import sys
import math
import time

def driving_mode(batt, num_seg, data):
    DISCOUNT = -1
    PETROL_PRICE = 2.0
    PETROL_KM = 10
    BATTERY_KM = 5
    MIN_BATT_LEVEL = 10.0

    BATTERY_CHARGE = [seg[0]/PETROL_KM * seg[1] for seg in data]
    PETROL_COST = [seg[0]/(PETROL_KM >> 1) for seg in data]
    BATTERY_DRAIN = [-seg[0]/BATTERY_KM for seg in data]
    PETROL_MODE = 'p'
    BATTERY_MODE = 'b'
    paths = []
    costs = []
    dp = [math.inf for i in range(num_seg + 1)]
    def driving_mode2(battLvl,mode,segNo,cost,battCharge,petrolCost,batteryDrain,cumPath):
        nonlocal dp, batt
        cumPath = cumPath + mode
        if segNo == len(battCharge):
            if mode == PETROL_MODE:
                battLvl += battCharge[segNo-1]
                cost += petrolCost[segNo-1]
            else:
                battLvl += batteryDrain[segNo-1]
            paths.append(cumPath)
            finalcost = cost + max(0,batt-battLvl)
            costs.append(finalcost)
            return finalcost
        
        if mode == PETROL_MODE:
            battLvl += battCharge[segNo-1]
            cost += petrolCost[segNo-1]
            
            if battLvl - 1 < MIN_BATT_LEVEL:
                petrol = driving_mode2(battLvl,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
                return petrol
            else:

                petrol = driving_mode2(battLvl,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
                battery = driving_mode2(battLvl + DISCOUNT,BATTERY_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
                return min(petrol, battery)
        else:
            battLvl += batteryDrain[segNo-1]
            
            if battLvl < MIN_BATT_LEVEL:
                petrol = driving_mode2(battLvl + DISCOUNT,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
                return petrol
            else:
                petrol = driving_mode2(battLvl + DISCOUNT,PETROL_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
                battery = driving_mode2(battLvl,BATTERY_MODE,segNo+1,cost,battCharge,petrolCost,batteryDrain,cumPath)
                return min(petrol, battery)

    # driver code
    if batt - 1 >= MIN_BATT_LEVEL:
        petrol = driving_mode2(batt + DISCOUNT,PETROL_MODE,1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN,'')
        battery = driving_mode2(batt + DISCOUNT,BATTERY_MODE,1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN,'')
        c = min(petrol, battery)
    else:
        c = driving_mode2(batt + DISCOUNT,PETROL_MODE,1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN,'')
    #print('DP = ',dp)
    # print(paths)
    #print(costs)
    print(paths[costs.index(c)], len(paths))
    return c

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    #batt, num_seg = float(s[0]) / 100, int(s[1])
    batt, num_seg = float(s[0]) , int(s[1])

    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i+2].split(':')])
    start_time = time.time()
    print('%.2f' % driving_mode(batt, num_seg, data))
    print("--- %s seconds ---" % (time.time() - start_time)) 


'''
import random as rd
rd.seed(47)
print(" ".join(["{0}:{1}".format(rd.randint(1,40),rd.randint(80,120)/100) for _ in range(15)]))

'''