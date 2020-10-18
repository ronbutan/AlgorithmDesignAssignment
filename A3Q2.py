import sys

def driving_mode(batt, num_seg, data):
    PETROL_PRICE = 2.0
    PETROL_KM = 10.0
    BATTERY_KM = 5.0
    MIN_BATT_LEVEL = 10.0

    BATTERY_CHARGE = [seg[0]/PETROL_KM * seg[1] for seg in data]
    PETROL_COST = [seg[0]/PETROL_KM * PETROL_PRICE for seg in data]
    BATTERY_DRAIN = [-seg[0]/BATTERY_KM for seg in data]
    # def driving_mode2(battLvl,mode,segNo,cost,battCharge,petrolCost,batteryDrain):
    #     if segNo == len(battCharge):
    #         if mode == 'p':
    #             battLvl += battCharge[segNo-1]
    #             cost += petrolCost[segNo-1]
    #         else:
    #             battLvl += batteryDrain[segNo-1]
    #         return cost + max(0,batt-battLvl)
        

    #     if mode == 'p':
    #         battLvl += battCharge[segNo-1]
    #         cost += petrolCost[segNo-1]
    #         if battLvl - 1 < MIN_BATT_LEVEL:
    #             return driving_mode2(battLvl,'p',segNo+1,cost,battCharge,petrolCost,batteryDrain)
    #         else:
    #             return min(driving_mode2(battLvl,'p',segNo+1,cost,battCharge,petrolCost,batteryDrain),driving_mode2(battLvl-1,'b',segNo+1,cost,battCharge,petrolCost,batteryDrain))
    #     else:
    #         battLvl += batteryDrain[segNo-1]
    #         if battLvl < MIN_BATT_LEVEL:
    #             return driving_mode2(battLvl - 1,'p',segNo+1,cost,battCharge,petrolCost,batteryDrain)
    #         else:
    #             return min(driving_mode2(battLvl - 1,'p',segNo+1,cost,battCharge,petrolCost,batteryDrain),driving_mode2(battLvl,'b',segNo+1,cost,battCharge,petrolCost,batteryDrain))

    
    # if batt - 1 >= MIN_BATT_LEVEL:
    #     return min(driving_mode2(batt-1,'p',1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN),driving_mode2(batt-1,'b',1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN))
    # else:
    #     return driving_mode2(batt-1,'p',1,0,BATTERY_CHARGE,PETROL_COST,BATTERY_DRAIN)

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    #batt, num_seg = float(s[0]) / 100, int(s[1])
    batt, num_seg = float(s[0]) , int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i+2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))
