import sys

def driving_mode(batt, num_seg, data):
    lstRoadDist = []
    lstChargeRate = []
    for item in data:
        lstRoadDist.append(item[0])
        lstChargeRate.append(item[1])
    PETROL_COST = 2.0
    BATT_COST = 1.0
    PETROL_UNIT_DIST = 10.0
    BATT_UNIT_DIST = 5.0
    pCost = 0.0
    bCost = 0.0
    batteryAux = [0 for i in range(num_seg)]
    petrolAux = [0 for i in range(num_seg)]
    charge = 0.0
    pRemainder = 0.0
    bRemainder = 0.0
    for i in range(0, num_seg):
        # petrol mode
        pCost = (lstRoadDist[i] / PETROL_UNIT_DIST) * PETROL_COST
        if i == 0:
            pRemainder = batt - 0.01
        charge = (lstRoadDist[i] / PETROL_UNIT_DIST) * 0.01 * lstChargeRate[i]
        print(charge)
        pRemainder += charge
        pCost += batt - pRemainder if batt > pRemainder else 0
        petrolAux[i] = pCost

        # battery mode
        if i == 0:
            bRemainder = batt - 0.01 - (lstRoadDist[i] / BATT_UNIT_DIST * 0.01)
        else:
            bRemainder -= (lstRoadDist[i] / BATT_UNIT_DIST * 0.01)
        bCost = (batt - bRemainder) * 100 if batt > bRemainder else 0
        batteryAux[i] = bCost
    print(petrolAux)
    print(batteryAux)
    return 0.0

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    batt, num_seg = float(s[0]) / 100, int(s[1])
    data = []
    print(batt)
    for i in range(num_seg):
        data.append([float(t) for t in s[i+2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))
