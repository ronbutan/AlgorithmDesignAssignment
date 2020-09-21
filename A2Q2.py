import sys
import math

class Node:
    def __init__ (self, id, cost, revenue):
        self._id = id
        self._cost = cost
        self._revenue = revenue
        self._profit = revenue - cost
        self._isavailable = 1
    def __str__(self):
        return "{0}:{1}:{2}".format(self._cost,self._revenue,self._profit)
    def __lt__(self,other):
        return self._cost < other._cost
    def __ge__(self, other):
        return self._cost >= other._cost
    def __gt__(self, other):
        return self._cost > other._cost
    def __repr__(self):
        return self.__str__()
class Heap:
    def __init__ (self, lst):
        self.__size = len(lst)
        self.__capacity = 2 ** math.ceil(math.log(self.__size + 1, 2))
        self.__content = [None] * self.__capacity
        for i in range(self.__size):
            self.__content[i+1] = lst[i]
    def __try_swap (self, i, j):
        if self.__content[j] > self.__content[i]:
            self.__content[i], self.__content[j] = self.__content[j], self.__content[i]
            return True
        else:
            return False
    def __heapify_at (self, i):
        if 2*i > self.__size:
            return
        if 2*i == self.__size or self.__content[2*i] >= self.__content[2*i+1]:
            if self.__try_swap(i, 2*i):
                self.__heapify_at(2*i)
        else:
            if self.__try_swap(i, 2*i+1):
                self.__heapify_at(2*i+1)
    def heapify (self):
        for i in range (self.__size // 2, 0, -1):
            self.__heapify_at(i)
    def insert (self, k):
        if self.__size + 1 == self.__capacity:
            self.__content.extend([None] * self.__capacity)
            self.__capacity *= 2
        self.__size += 1
        i = self.__size
        self.__content[i] = k
        while i > 1 and self.__try_swap(i // 2, i):
            i = i // 2
    def pop (self):
        if self.__size == 0:
            return None
        else:
            k = self.__content[1]
            self.__content[1], self.__content[self.__size] = self.__content[self.__size], None
            self.__size -= 1
            self.__heapify_at(1)
            return k
    def len (self):
        return self.__size
    def print (self):
        print ('the content is', self.__content[1:self.__size+1])

# def project_selection2(c,k,l):
#     if k == 0:
#         return 0
#     isFullList = 0
#     for i in range(len(l)):
#         if i == len(l) - 1:
#             isFullList = 1
#         if l[i]._isavailable == 0:
#             continue
#         if l[i]._cost > c:
#             break
#     if isFullList:
#         i+= 1
#     lstprofit = [p._profit for p in l[:i]]
#     print(lstprofit)
#     areSame = all(elem == 0 for elem in lstprofit)
#     if areSame:
#         return -1
#     maxprofit = max(lstprofit)
#     c += maxprofit
#     idx = lstprofit.index(maxprofit)
#     l[idx]._isavailable = 0
#     l[idx]._profit = 0
#     nextprofit = project_selection2(c,k-1,l)
#     if nextprofit == -1:
#         return -1
#     else:
#         return maxprofit + nextprofit

def project_selection2(c,k,l,idx,h):
    if k == 0:
        return c
    nextproject = None
    for i in range(idx,len(l)):
        if l[i]._cost <= c:
            h.insert(l[i]._profit)
            if (i + 1 == len(l)):
                nextproject = h.pop()
        else:
            nextproject = h.pop()
            break
    
    if nextproject is None:
        return -1
    else:
        c += nextproject
        return project_selection2(c,k-1,l,i,h)


def project_selection(c, k):
    global cr
    numprojects = len(cr)
    lstprojects = [Node(p, cr[p][0], cr[p][1]) for p in range(numprojects)]
    lstprojects.sort()
    print(lstprojects)
    # start recursion
    #m = project_selection2(c,k,lstprojects)
    h = Heap([])
    m = project_selection2(c,k,lstprojects,0,h)
    return 'impossible' if m == -1 else m

a = [int(s) for s in sys.stdin.readline().split()]
cr = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
for _ in range(a[1]):
    b = [int(s) for s in sys.stdin.readline().split()]
    c, k = b[0], b[1]
    print(project_selection(c, k))

