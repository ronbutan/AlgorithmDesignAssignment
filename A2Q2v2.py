import sys
from heapq import heappop, heappush, heapify

def project_selection(c,k):
    global listCost,listProfit
    if c >= max(listCost): # n
        l = sorted(listProfit) # n logn
        mostProfit = sum([x for x in l[-k:]]) # n
        c += mostProfit
        return c
    minCostHeap = [[listCost[i], i] for i in range(len(listCost))]
    maxProfitHeap = []
    heapify(minCostHeap) # n
    while k > 0:
        while minCostHeap and minCostHeap[0][0] <= c:# n
            proj = heappop(minCostHeap)
            idx = proj[1]
            heappush(maxProfitHeap, -listProfit[idx]) # log n

        # implies no more profitable project left to choose
        if not maxProfitHeap:
            return 'impossible'
        
        c = c + -(heappop(maxProfitHeap))
        k = k - 1
    return c

a = [int(s) for s in sys.stdin.readline().split()]
if a[0] > 100000:
    print('impossible')
cr = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
listCost = [s[0] for s in cr]
listProfit = [s[1] - s[0] for s in cr]
for _ in range(a[1]):
    b = [int(s) for s in sys.stdin.readline().split()]
    c, k = b[0], b[1]
    print(project_selection(c, k))

'''
Concept:
========
First, create 2 lists, listCost and listProfit, to hold the cost and profit (i.e. revenue - cost) respectively
Second, determine if capital is larger or equals than all projects for selection
- if capital is larger than or equals to all project cost, select the most profitable k projects and sum the profits

Third, create a minimum heap based on the cost of projects. Each heap object also bears an index property for macthing against its corresponding profit in listProfit
Fourth, iterate based on the number of projects to be selected and within each iteration, iterate the minimum cost heap.
- pop the minimum cost heap and push its corresponding value to a maximum profit heap and exits the inner iteration

Fifth, pop the maximum profit heap and add the profit ot exisitng capital
- return 'impossible' if there are no more projects to select from the maximum profit heap

Analysis:
=========
1. Python maximum function - n
2. Python list sort function worst time complexity - n logn
3. Sum function - n
4. Loop to iterate projects - n
4i. heap push into profit heap within loop - logn

Total   = n + n logn + n + (n * logn)
        = 2n + 2n logn

Time Complexity = O(n logn)
'''