import sys
import time
import heapq

def escape(n, roadmap, qrtn, spaceship):
    RESULT = [0 if i+1 in spaceship else float('inf') for i in range(n + 1)]
    lstRemainingCities = [i for i in range(1,n + 1) if i not in spaceship]
    spaceshipindex = [True if i in spaceship else False for i in range(0, n + 1)]
    unvisited = []
    lstRemoval = []
    GREEN = 'G'
    ORANGE = 'O'
    RED = 'R'
    
    # for id in spaceship:
    #     spaceshipcity = roadmap[id]
    #     for city,blinks in spaceshipcity.items():
    #         if blinks < 0:
    #             RESULT[city] = min(RESULT[city], abs(blinks) + qrtn[id][1])
    #         else:
    #             RESULT[city] = min(RESULT[city], blinks)
    #         lstRemoval.append(city)
    # lstRemainingCities = [i for i in lstRemainingCities if i not in lstRemoval]
    for id in lstRemainingCities:
        unvisited = []
        neighbours = roadmap[id]
        for city in range(1,n + 1):
            if city != id:
                blinks = neighbours.get(city, 0)
                if blinks >= 0:
                    heapq.heappush(unvisited, [blinks, city, GREEN] if city in neighbours else [float('inf'),city,GREEN])
                else:
                    blinks = abs(blinks)
                    heapq.heappush(unvisited, [blinks, city, ORANGE] if city in neighbours else [float('inf'),city,GREEN])
                    heapq.heappush(unvisited, [blinks + qrtn[city][1], city, GREEN] if city in neighbours else [float('inf'),city,GREEN])
        while unvisited:
            mindist, v, health = heapq.heappop(unvisited)
            if spaceshipindex[v]:
                if health == GREEN:
                    RESULT[id] = min(RESULT[id], mindist)
                elif health == ORANGE:
                    RESULT[id] = min(RESULT[id], mindist + qrtn[v][1])
                else:
                    RESULT[id] = min(RESULT[id], mindist + qrtn[v][0] + qrtn[v][1])
                break
            newPoints = []
            for i in range(len(unvisited)):
                c = unvisited[i][1]
                if c in roadmap[v]:
                    blinks = roadmap[v][c]
                    if health == GREEN and blinks < 0:
                        if (unvisited[i][2] == GREEN and unvisited[i][0] == float('inf')) or (unvisited[i][2] == ORANGE):
                            unvisited[i][2] = ORANGE
                            unvisited[i][0] = min(unvisited[i][0], mindist + abs(blinks))

                            l = list(filter(lambda x: x[1] == c and x[2] == GREEN and x[0] < float('inf'), unvisited))
                            if not l:
                                d = mindist + abs(blinks) + qrtn[unvisited[i][1]][1]
                                new = [d, c, GREEN]
                                newPoints.append(new)
                            else:
                                idx = unvisited.index(l[0])
                                unvisited[idx][2] = GREEN
                                unvisited[idx][0] = min(unvisited[idx][0], mindist + abs(blinks) + qrtn[unvisited[idx][1]][1])
                    elif health == ORANGE and blinks < 0:
                        if unvisited[i][2] == GREEN and unvisited[i][0] == float('inf'):
                            unvisited[i][2] = ORANGE
                            unvisited[i][0] = min(unvisited[i][0], mindist + abs(blinks) + qrtn[c][0])
                            l = list(filter(lambda x: x[1] == c and x[2] == GREEN and x[0] < float('inf'), unvisited))
                            if not l:
                                d = mindist + abs(blinks) + qrtn[c][1] + qrtn[c][0]
                                new = [d, c, GREEN]
                                newPoints.append(new)
                            else:
                                idx = unvisited.index(l[0])
                                unvisited[idx][2] = GREEN
                                unvisited[idx][0] = min(unvisited[idx][0], mindist + abs(blinks) + qrtn[unvisited[idx][1]][1] + qrtn[c][0])
                    else:
                        if (unvisited[i][2] == GREEN and unvisited[i][0] == float('inf')) or (unvisited[i][2] == health):
                            unvisited[i][0] = min(unvisited[i][0], mindist + abs(blinks))
                            unvisited[i][2] = health
                            
                            if health == ORANGE:
                                l = list(filter(lambda x: x[1] == c and x[2] == GREEN and x[0] < float('inf'), unvisited))
                                if not l:
                                    d = mindist + abs(blinks) + qrtn[c][1]
                                    new = [d, c, GREEN]
                                    newPoints.append(new)
                                else:
                                    idx = unvisited.index(l[0])
                                    unvisited[idx][2] = GREEN
                                    unvisited[idx][0] = min(unvisited[idx][0], mindist + abs(blinks) + qrtn[c][1])
            for i in newPoints:
                heapq.heappush(unvisited,i)
            heapq.heapify(unvisited)
    return RESULT[1:]

n = int(sys.stdin.readline())
#roadmap = {}
roadmap = {i:{} for i in range(1,n + 1)}
s = sys.stdin.readline().split()
for t in s:
    u = t.split(':')
    roadmap[int(u[0])][int(u[1])] = int(u[2])
    roadmap[int(u[1])][int(u[0])] = int(u[2])
    #roadmap[int(u[0]), int(u[1])] = int(u[2])
qrtn = [0] * (n + 1)
s = sys.stdin.readline().split()
i = 1
for t in s:
    u = t.split(':')
    qrtn[i] = int(u[0]), int(u[1])
    i += 1
spaceship = [int(t) for t in sys.stdin.readline().split()]
start_time = time.time()
print(' '.join([str(i) for i in escape(n, roadmap, qrtn, spaceship)]))
print("--- %s seconds ---" % (time.time() - start_time))
