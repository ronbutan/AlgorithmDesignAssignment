import sys
from decimal import *
import time


def optimize(temp_result):
    new_temp_result = []
    sorted_temp_result = sorted(temp_result)
    for i in range(len(sorted_temp_result)):
        battery, fuel_cost = sorted_temp_result[i]
        if battery == 100:
            new_temp_result.append((battery, fuel_cost))
            break
        can_optimize = True

        for j in range(i + 1, len(sorted_temp_result)):
            c_battery, c_fuel_cost = sorted_temp_result[j]
            if c_fuel_cost < fuel_cost:
                can_optimize = False
                break
        if can_optimize:
            new_temp_result.append((battery, fuel_cost))
    return new_temp_result


def optimize_further(temp_result_battery, temp_result_petrol):
    redundant_temp_result_battery = set()
    redundant_temp_result_petrol = set()
    for battery_battery, battery_cost in temp_result_battery:
        for petrol_battery, petrol_cost in temp_result_petrol:
            if battery_battery >= 11 and battery_battery - 1 >= petrol_battery and battery_cost <= petrol_cost:
                redundant_temp_result_petrol.add((petrol_battery, petrol_cost))
            if petrol_battery >= 11 and petrol_battery - 1 >= battery_battery and petrol_cost <= battery_cost:
                redundant_temp_result_battery.add((battery_battery, battery_cost))
    for x in redundant_temp_result_battery:
        temp_result_battery.remove(x)
    for y in redundant_temp_result_petrol:
        temp_result_petrol.remove(y)


def driving_mode(batt, num_seg, data):
    # One route for each trip
    # Cars always stop before crossings and only before crossings.
    # Cars only switch mode when it is stopped. 1% of the curr_battery is needed
    # Starting the car needs 1%
    # Cars cannot switch to curr_battery mode if the current curr_battery level is < 11%
    # Cars must switch to petrol if curr_battery is < 10%, before pedestrian crossing
    # Flat - 1%, up slopes - 0.8%, down - 1.2%
    # 1 liter of petrol travel 10KM, which costs $2
    # 1% curr_battery = 5KM, which costs 1 dollar => so 2% costs 10KM, which costs 2 dollar
    # You need to charge curr_battery level back to 85%
    # You need to pay for the patrol cost

    battery_switch_mode_cost = 1
    battery_switch_limit = 11
    battery_start_car_cost = 1
    battery_charge_unit = 10  # 1% per 10 KM
    battery_maximum = 100
    battery_per_unit_distance = 5
    petrol_per_liter_price = 2
    petrol_per_liter_distance = 10
    petrol_price_per_km = petrol_per_liter_distance / petrol_per_liter_price

    # road segments s are <= 100
    # distance of road segment di <= 40
    max_road_segment = 100
    max_distance_per_road_segment = 40

    distance = Decimal(data[0][0])
    battery_charge_rate = Decimal(data[0][1])
    battery_addition = Decimal(distance) / Decimal(10) * Decimal(battery_charge_rate)
    fuel_cost = Decimal(distance) / Decimal(5)
    battery_mode_usage = Decimal(distance) / Decimal(5)
    temp_petrol_result = [(min(batt - 1 + battery_addition, 100), fuel_cost)]
    temp_battery_result = []
    if batt >= 11:
        battery_updated = batt - 1 - battery_mode_usage
        temp_battery_result.append((battery_updated, 0))

    for i in range(1, num_seg):
        distance = data[i][0]
        battery_charge_rate = data[i][1]
        battery_addition = Decimal(distance) / Decimal(10) * Decimal(battery_charge_rate)
        fuel_cost = Decimal(distance) / Decimal(5)
        battery_mode_usage = Decimal(distance) / Decimal(5)
        petrol_combinations = []
        battery_combinations = []

        temp_battery_result = optimize(temp_battery_result)
        temp_petrol_result = optimize(temp_petrol_result)
        optimize_further(temp_battery_result, temp_petrol_result)

        for battery, cost in temp_battery_result:
            # battery after battery
            if battery >= 10:
                battery_combinations.append((battery - battery_mode_usage, cost))
            # petrol after battery
            petrol_combinations.append((min(battery - 1 + battery_addition, 100), cost + fuel_cost))
        for battery, cost in temp_petrol_result:
            # battery after petrol:
            if battery >= 11:
                battery_combinations.append((battery - battery_mode_usage - 1, cost))
            # petrol after petrol
            petrol_combinations.append((min(battery + battery_addition, 100), cost + fuel_cost))

        temp_petrol_result = petrol_combinations.copy()
        temp_battery_result = battery_combinations.copy()

    All_Combinations = []
    All_Combinations.extend(petrol_combinations)
    All_Combinations.extend(battery_combinations)
    return min([total_fuel_cost + max((batt - battery_end), 0) for battery_end, total_fuel_cost, in
                All_Combinations])


def round_number_times(num, times, floor=2):
    r = num
    while times >= floor:
        r = round(r, times)
        times = times - 1
    return r


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    batt, num_seg = Decimal(s[0]), int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i + 2].split(':')])
    start_time = time.time()
    print(round_number_times(driving_mode(batt, num_seg, data), 7))
    print("--- %s seconds ---" % (time.time() - start_time)) 
    """
    case_1 = "85 3 3:0.88 5:1.09 30:1".split()  # 6.60 => battery mode for the first 2 segments and petrol mode for the last
    batt, num_seg = float(case_1[0]), int(case_1[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in case_1[i + 2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))
    """
