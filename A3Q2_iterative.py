import sys,time
def driving_mode(batt, num_seg, data):
    '''
    Parameters
    ----------
    batt     : Original battery level (in percentage)
    num_seg  : Number of stops
    data     : List containing the distance of segment and battery conversion rate

    Returns
    -------
    Incurred charges for minimum cost path

    '''
    # Loop through each road segment #
    for i in range(num_seg):
        ## Compute charged capacity for petrol option ##
        charge = data[i][0] / 10 * data[i][1]
        ## Compute fuel cost, regardless of fuel option ##
        fuel_cost = data[i][0] / 5
        
        ## First segment ##
        if i == 0:
            ### Initialise a temp list ###
            temp = []
            ### Initialise battery first option ###
            if batt - 1 >= 10:
                temp.append((1 + fuel_cost, batt - 1 - fuel_cost, 0))
            ### Initialise petrol first option ###
            temp.append((fuel_cost + max(0, batt - (batt - 1 + charge)), 
                         min(batt - 1 + charge, 100), 
                         1))
        
        ## Subsequent segments ##
        else:
            combined = []
            for cum_cost, curr_batt, curr_fuel in temp:
                if curr_batt >= 10:
                    ### Mandatory battery option ###
                    if curr_batt > batt: 
                        if curr_fuel == 0:
                            increment_cost = max(0, batt - (curr_batt - fuel_cost))
                            combined.append((cum_cost + min(fuel_cost, increment_cost), 
                                             min(curr_batt - fuel_cost, 100), 
                                             0))
                        else:
                            increment_cost = max(0, batt - (curr_batt - 1 - fuel_cost))
                            combined.append((cum_cost + min(1 + fuel_cost, increment_cost),
                                             min(curr_batt - 1 - fuel_cost, 100), 
                                             0))
                    
                    ### Choice of fuel ###
                    else:
                        if curr_fuel == 0:
                            increment_cost = max(0, batt - (curr_batt - fuel_cost))
                            combined.append((cum_cost + min(fuel_cost, increment_cost), 
                                             min(curr_batt - fuel_cost, 100), 
                                             0))
                            if curr_batt - 1 >= batt:
                                batt_rebate = 0
                            elif curr_batt - 1 + charge >= batt:
                                batt_rebate = batt - curr_batt
                            else:
                                batt_rebate = charge - 1
                            combined.append((cum_cost + fuel_cost - batt_rebate,
                                             min(curr_batt - 1 + charge, 100),
                                             1))
                        else:
                            increment_cost = max(0, batt - (curr_batt - 1 - fuel_cost))
                            combined.append((cum_cost + min(1 + fuel_cost, increment_cost),
                                             min(curr_batt - 1 - fuel_cost, 100), 
                                             0))
                            if curr_batt >= batt:
                                batt_rebate = 0
                            elif curr_batt + charge >= batt:
                                batt_rebate = batt - curr_batt
                            else:
                                batt_rebate = charge
                            combined.append((cum_cost + fuel_cost - batt_rebate,
                                             min(curr_batt + charge, 100),
                                             1))
                    
                ### Mandatory petrol option ###
                else:
                    if curr_fuel == 0:
                        if curr_batt - 1 >= batt:
                            batt_rebate = 0
                        elif curr_batt - 1 + charge >= batt:
                            batt_rebate = batt - curr_batt
                        else:
                            batt_rebate = charge - 1
                        combined.append((cum_cost + fuel_cost - batt_rebate,
                                         min(curr_batt - 1 + charge, 100),
                                         1))       
                    else:
                        if curr_batt >= batt:
                            batt_rebate = 0
                        elif curr_batt + charge >= batt:
                            batt_rebate = batt - curr_batt
                        else:
                            batt_rebate = charge
                        combined.append((cum_cost + fuel_cost - batt_rebate,
                                         min(curr_batt + charge, 100),
                                         1)) 

            ## Initialise the temp and combined lists ##
            temp = combined.copy()
            combined = None
    #print(temp)                      
    #print('Length',len(temp))
    return min([cost for cost, curr_batt, curr_fuel in temp])

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

