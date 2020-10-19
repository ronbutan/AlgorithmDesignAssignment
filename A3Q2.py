import sys

def driving_mode(batt, num_seg, data):
    PETROL_PRICE = 2.0
    PETROL_KM = 10.0
    BATTERY_KM = 5.0
    MIN_BATT_LEVEL = 10.0

    BATTERY_CHARGE = [seg[0]/PETROL_KM * seg[1] for seg in data]
    PETROL_COST = [seg[0]/PETROL_KM * PETROL_PRICE for seg in data]
    BATTERY_DRAIN = [-seg[0]/BATTERY_KM for seg in data]
    PETROL_MODE = 'p'
    BATTERY_MODE = 'b'
    paths = []
    costs = []
    dp = [[float('inf') for seg in data] for seg in data]

    
    def driving_mode2(battLvl,mode,segNo,cost,battCharge,petrolCost,batteryDrain,cumPath):
        cumPath = cumPath + mode
        if segNo == len(battCharge):
            if mode == PETROL_MODE:
                battLvl += battCharge[segNo-1]
                cost += petrolCost[segNo-1]
            else:
                battLvl += batteryDrain[segNo-1]
            paths.append(cumPath)
            costs.append(cost + max(0,batt-battLvl))
            return cost + max(0,batt-battLvl)
        

        if mode == PETROL_MODE:
            battLvl += battCharge[segNo-1]
            cost += petrolCost[segNo-1]
            if battLvl - 1 < MIN_BATT_LEVEL:
                return driving_mode2(battLvl,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
            else:
                return min(driving_mode2(battLvl,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath),driving_mode2(battLvl-1,BATTERY_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath))
        else:
            battLvl += batteryDrain[segNo-1]
            if battLvl < MIN_BATT_LEVEL:
                return driving_mode2(battLvl - 1,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
            else:
                return min(driving_mode2(battLvl - 1,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath),driving_mode2(battLvl,BATTERY_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath))

    # driver code
    if batt - 1 >= MIN_BATT_LEVEL:
        c = min(driving_mode2(batt-1,PETROL_MODE,1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN,''),driving_mode2(batt-1,BATTERY_MODE,1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN,''))
        print(paths[costs.index(c)])
        return c
    else:
        c = driving_mode2(batt-1,PETROL_MODE,1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN,'')
        print(paths[costs.index(c)])
        return c

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    #batt, num_seg = float(s[0]) / 100, int(s[1])
    batt, num_seg = float(s[0]) , int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i+2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))
