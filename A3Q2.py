import sys
import time

class TravelNode:
    def __init__ (self, batt, cost, mode):
        self._batt = batt
        self._cost = cost
        self._mode = mode
        self._totalcost = float('inf')
    def totalcost(self, batt):
        self._totalcost = self._cost + max(batt - self._batt, 0)
        return self._totalcost
    def __str__(self):
        return "{0}:{1}:{2}".format(self._batt,self._cost,self._mode)
    def __hash__(self):
        return hash((self._batt, self._cost))
    def __le__(self, other):
        if self._batt == other._batt:
            return self._cost <= other._cost
        return self._batt <= other._batt
    def __lt__(self,other):
        if self._batt == other._batt:
            return self._cost < other._cost
        return self._batt < other._batt
    def __ge__(self, other):
        return self._batt >= other._battt
    def __gt__(self, other):
        if self._batt == other._batt:
            return self._cost > other._cost
        return self._batt > other._batt
    def __eq__(self, other):
        return self._batt == other._batt and self._cost == other._cost
    def __repr__(self):
        return self.__str__()

def validateNode(l, maxBatt):
    nLst = []
    l.sort()
    nLen = len(l)
    isPossible = True
    for i in range(nLen):
        isPossible = True
        pNode = l[i]
        # implies need not look further as all nodes will be at full charge and will require onward computation. Remaining nodes will have full charge and equal or greater cumulative cost
        if pNode._batt == maxBatt:
            nLst.append(pNode)
            break

        for j in range(i + 1, nLen):
            aNode = l[j]
            # implies pNode has lower battery level and higher cost than remaining nodes, so can ignore further onward computation from pNode
            if aNode._cost < pNode._cost:
                isPossible = False
                break
        if isPossible:
            nLst.append(pNode)
    return nLst

def driving_mode(batt, num_seg, data):
    '''
    Assume max battery charge of 100%
    '''
    DISCOUNT = -1.0
    PETROL_PRICE = 2.00
    PETROL_KM = 10
    BATTERY_KM = 5
    MIN_BATT_LEVEL = 10.0
    MAX_BATTERY = 100.0

    BATTERY_CHARGE = [seg[0]/PETROL_KM * seg[1] for seg in data]
    PETROL_COST = [seg[0]/PETROL_KM * PETROL_PRICE for seg in data]
    BATTERY_DRAIN = [-seg[0]/BATTERY_KM for seg in data]
    PETROL_MODE = 'p'
    BATTERY_MODE = 'b'
    ROUNDING = 0.00000000000004

    # Calculate information for first petrol and first battery node for first segment
    lstPetrolNode = []
    lstBatteryNode = []
    lstAllNodes = []
    lstPetrolNode = [TravelNode(min(batt + DISCOUNT + BATTERY_CHARGE[0], MAX_BATTERY), PETROL_COST[0], PETROL_MODE)]
    if batt >= MIN_BATT_LEVEL:
        lstBatteryNode = [TravelNode(batt + DISCOUNT + BATTERY_DRAIN[0], 0, BATTERY_MODE)]

    for i in range(1, num_seg):
        lstPetrolSegment = []
        lstBatterySegment = []

        for node in lstBatteryNode:
            if node._batt >= MIN_BATT_LEVEL:
                lstBatterySegment.append(TravelNode(node._batt + BATTERY_DRAIN[i], node._cost, node._mode + BATTERY_MODE))
            lstPetrolSegment.append(TravelNode(min(node._batt + DISCOUNT + BATTERY_CHARGE[i], MAX_BATTERY), node._cost + PETROL_COST[i], node._mode + PETROL_MODE))
        for node in lstPetrolNode:
            if node._batt + DISCOUNT >= MIN_BATT_LEVEL:
                lstBatterySegment.append(TravelNode(node._batt + DISCOUNT + BATTERY_DRAIN[i], node._cost, node._mode + BATTERY_MODE))
            lstPetrolSegment.append(TravelNode(min(node._batt + BATTERY_CHARGE[i], MAX_BATTERY), node._cost + PETROL_COST[i], node._mode + PETROL_MODE))

        lstBatteryNode = validateNode(lstBatterySegment, MAX_BATTERY)
        lstPetrolNode = validateNode(lstPetrolSegment, MAX_BATTERY)
        
    lstAllNodes.extend(lstPetrolNode)
    lstAllNodes.extend(lstBatteryNode)
    index = min(range(len(lstAllNodes)), key=lambda i: lstAllNodes[i].totalcost(batt))
    c = lstAllNodes[index]._totalcost
    c = c + ROUNDING
    return c

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    batt, num_seg = float(s[0]) , int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i+2].split(':')])
    #start_time = time.time()
    print('%.2f' % driving_mode(batt, num_seg, data))
    #print("--- %s seconds ---" % (time.time() - start_time)) 

