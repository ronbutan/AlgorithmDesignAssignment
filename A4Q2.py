import sys
import heapq
from collections import defaultdict

def escape(n, roadmap, qrtn, spaceship):
    spaceshipindex = [True if i in spaceship else False for i in range(n)]
    RESULT_STATUS = [i == 0 or spaceshipindex[i] for i in range(n)]
    RESULT = [0 if spaceshipindex[i] else float('inf') for i in range(n)]
    queue = []
    visited = defaultdict(int)
    seen = defaultdict(int)
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
            heapq.heappush(queue, [qrtn[cityId][1], cityOrangeKey])
            visited[cityGreenKey] = 1
        for neighbourId,blinks in neighbours:
            neighbourGreenKey, neighbourOrangeKey, neighbourRedKey = "{0}{1}".format(neighbourId, GREEN), "{0}{1}".format(neighbourId, ORANGE), "{0}{1}".format(neighbourId, RED)
            if blinks >= 0: # trusted, only O->O or G->G
                GRAPH[neighbourGreenKey][cityGreenKey] = blinks
                GRAPH[neighbourOrangeKey][cityOrangeKey] = blinks
                if spaceshipindex[cityId]:
                    computed = seen[neighbourGreenKey]
                    if computed == 0 or computed > blinks:
                        heapq.heappush(queue, [blinks, neighbourGreenKey])
                        seen[neighbourGreenKey] = blinks
            else: # untrusted, 0->G, R->O
                blinks = -blinks
                GRAPH[neighbourOrangeKey][cityGreenKey] = blinks
                GRAPH[neighbourRedKey][cityOrangeKey] = blinks
    while queue:
        mindist, v = heapq.heappop(queue)
        cityId = int(v[:-1], 10)
        health = v[-1]
        if visited[v] > 0 and not spaceshipindex[cityId]:
            continue
        visited[v] = 1
        seen[v] = mindist
        if health == GREEN:
            RESULT[cityId] = min(RESULT[cityId], mindist)
            RESULT_STATUS[cityId] = True
            if all(RESULT_STATUS):
                break
        neighbours = GRAPH[v].items()
        for neighbourId,blinks in neighbours:
            if visited[neighbourId] == 0:
                computed = seen[neighbourId]
                blinks += mindist
                if (computed == 0) or (computed > blinks):
                    heapq.heappush(queue, [blinks, neighbourId])
                    seen[neighbourId] = blinks
    return RESULT[1:]

n = int(sys.stdin.readline(), 10)
N = n + 1
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
print(' '.join([str(i) for i in escape(N, roadmap, qrtn, spaceship)]))

'''
Concept:
=========
1. Create a GRAPH of n * 3 nodes with each city expanded to its Green, Orange and Red states
2. Orange states will be connected by an edge with cost of Orange to Green quarantine blinks
3. Red states will be connected by an edge with cost of Red to Orange quarantine blinks
4. Allowed edges from trusted cities are Green to Green and Orange to Orange
5. Allowed edges from untrusted cities are Orange to Green and Red to Orange (reverse direction)
4. Run Dijkstra algorithm supported with a minimum heap
5. Start with spaceship cities and traverse to all other cities
6. We will capture results upon visiting a city in Green state
'''