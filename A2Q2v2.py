import sys

class Node:
    def __init__ (self, cost, revenue):
        self._cost = cost
        self._revenue = revenue
        self._profit = revenue - cost
    def __str__(self):
        return "{0}:{1}:{2}".format(self._cost,self._revenue,self._profit)
    def __le__(self, other):
        return self._cost <= other._cost
    def __lt__(self,other):
        return self._cost < other._cost
    def __ge__(self, other):
        return self._cost >= other._cost
    def __gt__(self, other):
        return self._cost > other._cost
    def __repr__(self):
        return self.__str__()

def project_selection2(c,k,lstprojects):
    # iterate backwards from most profitable projects
    while k and lstprojects:
        # reset pointer to end of list (most profitable project)
        i = len(lstprojects) - 1
        while i > -1 and lstprojects[i]._cost > c:
            i -= 1 # decrement pointer as insufficient capital
        if i < 0:
            return -1
        c += lstprojects[i]._profit
        lstprojects.pop(i)
        k -= 1
    return c

def project_selection(c, k):
    global cr
    numprojects = len(cr)
    lstprojects = [Node(cr[p][0], cr[p][1]) for p in range(numprojects)]
    lstprojects.sort(key=lambda x: x._profit)
    m = project_selection2(c,k,lstprojects)
    return 'impossible' if m == -1 else m

a = [int(s) for s in sys.stdin.readline().split()]
if a[0] > 100000:
    print('impossible')
cr = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
for _ in range(a[1]):
    b = [int(s) for s in sys.stdin.readline().split()]
    c, k = b[0], b[1]
    print(project_selection(c, k))

'''
Concept:
========
First, represent each project as a Node with properties Cost, Revenue and Profit
Second, sort list of Node objects by profit (most profitable at the end of list)
Third, iterate through the list of projects selecting the most profitable project that can be undertaken based on current captial
Fourth, iteration stops upon the number of projects fulfilled or there are no more projects left for selection

Analysis:
=========
1. List sort on profit based on worst case time complexity - n logn
2. Outer loop to loop based on number of projects to be selected, k and number of projects left for selection - n
3. Inner loop to pick next most profitable project based on current available capital - n

Total   = n logn + (n * n)
        = n^2 + n logn

Time Complexity = O(n^2)

'''