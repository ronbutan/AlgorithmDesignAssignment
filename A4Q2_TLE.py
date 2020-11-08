import sys
import time
import heapq
from collections import defaultdict

def escape(n, roadmap, qrtn, spaceship):
    spaceshipindex = [True if i in spaceship else False for i in range(n)]
    RESULT_STATUS = [i == 0 for i in range(n)]
    RESULT = [0 if spaceshipindex[i] else float('inf') for i in range(n)]
    queue = []
    visited = defaultdict(int)
    GREEN = 'G'
    ORANGE = 'O'
    RED = 'R'
    GRAPH = defaultdict(lambda: defaultdict(dict))
    
    for cityId in range(1, n):
        neighbours = roadmap[cityId].items()
        cityGreenKey, cityOrangeKey, cityRedKey = "{0}{1}".format(cityId, GREEN), "{0}{1}".format(cityId, ORANGE), "{0}{1}".format(cityId, RED)
        GRAPH[cityGreenKey][cityOrangeKey] = qrtn[cityId][1]
        GRAPH[cityOrangeKey][cityRedKey] = qrtn[cityId][0]

        if spaceshipindex[cityId]:
            heapq.heappush(queue, [0, cityGreenKey])
        for neighbourId,blinks in neighbours:
            neighbourGreenKey, neighbourOrangeKey, neighbourRedKey = "{0}{1}".format(neighbourId, GREEN), "{0}{1}".format(neighbourId, ORANGE), "{0}{1}".format(neighbourId, RED)
            if blinks >= 0: # trusted, only O->O or G->G
                GRAPH[neighbourGreenKey][cityGreenKey] = blinks
                GRAPH[neighbourOrangeKey][cityOrangeKey] = blinks
            else: # untrusted, 0->G, R->O
                blinks = -blinks
                GRAPH[neighbourOrangeKey][cityGreenKey] = blinks
                GRAPH[neighbourRedKey][cityOrangeKey] = blinks
    while queue:
        mindist, v = heapq.heappop(queue)
        cityId = int(v[:-1], 10)
        health = v[-1]
        visited[v] = 1
        if health == GREEN:
            RESULT[cityId] = min(RESULT[cityId], mindist)
            RESULT_STATUS[cityId] = True
            if all(RESULT_STATUS):
                break
        neighbours = GRAPH[v].items()
        for neighbourId,blinks in neighbours:
            if visited[neighbourId] == 0:
                blinks += mindist
                heapq.heappush(queue, [blinks, neighbourId])
        #print(queue)
    return RESULT[1:]

n = int(sys.stdin.readline(), 10)
N = n + 1
#roadmap = defaultdict(lambda: defaultdict(dict))
roadmap = {i:{} for i in range(1, N)}
s = sys.stdin.readline().split()
for t in s:
    u = t.split(':')
    c1 = int(u[0], 10)
    c2 = int(u[1], 10)
    d = int(u[2], 10)
    roadmap[c1][c2] = d
    roadmap[c2][c1] = d
qrtn = [0] * N
s = sys.stdin.readline().split()
i = 1
for t in s:
    u = t.split(':')
    qrtn[i] = int(u[0], 10), int(u[1], 10)
    i += 1
spaceship = [int(t, 10) for t in sys.stdin.readline().split()]
#start_time = time.time()
print(' '.join([str(i) for i in escape(N, roadmap, qrtn, spaceship)]))
#print("--- %s seconds ---" % (time.time() - start_time))