import sys
import math
from heapq import heapify, heappop, heappush

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
class MaxHeap:
    def __init__ (self, lst):
        self.__size = len(lst)
        self.__capacity = 2 ** math.ceil(math.log(self.__size + 1, 2))
        self.__content = [None] * self.__capacity
        for i in range(self.__size):
            self.__content[i+1] = lst[i]
    def __try_swap (self, i, j):
        if self.__content[j]._profit > self.__content[i]._profit:
            self.__content[i], self.__content[j] = self.__content[j], self.__content[i]
            return True
        else:
            return False
    def __heapify_at (self, i):
        if 2*i > self.__size:
            return
        if 2*i == self.__size or self.__content[2*i]._profit >= self.__content[2*i+1]._profit:
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

class MinHeap:
    def __init__ (self, lst):
        self.__size = len(lst)
        self.__capacity = 2 ** math.ceil(math.log(self.__size + 1, 2))
        self.__content = [None] * self.__capacity
        for i in range(self.__size):
            self.__content[i+1] = lst[i]
    def __try_swap (self, i, j):
        if self.__content[j]._cost < self.__content[i]._cost:
            self.__content[i], self.__content[j] = self.__content[j], self.__content[i]
            return True
        else:
            return False
    def __heapify_at (self, i):
        if 2*i > self.__size:
            return
        if 2*i == self.__size or self.__content[2*i]._cost <= self.__content[2*i+1]._cost:
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
    def head(self):
        return self.__content[1]
    def print (self):
        print ('the content is', self.__content[1:self.__size+1])

# def project_selection2(c, k, l):
#     if c > l[-1]._cost:
#         c = c + sum([x._profit for x in l[-k:]])
#         return c
#     minHeap = [[l[x]._cost, x] for x in range(len(l))]
#     maxHeap = []
#     heapify(minHeap)
#     while k:
#         while minHeap and minHeap[0][0]<=c:
#             a,idx = heappop(minHeap)
#             heappush(maxHeap, -l[idx]._profit)
        
#         if not maxHeap:
#             return "impossible"
        
#         c = c - heappop(maxHeap)
#         k = k - 1
#     return c

# def project_selection2(c,k,l):
#     if c >= l[-1]._cost:
#         c = c + sum([x._profit for x in l[-k:]])
#         return c
#     minHeap = MinHeap(l)
#     maxHeap = MaxHeap([])
#     minHeap.heapify()
#     while k > 0:
#         while minHeap.len() > 0 and minHeap.head()._cost <= c:
#             p = minHeap.pop()
#             maxHeap.insert(p)

#         if maxHeap.len() == 0:
#             return -1
#         else:
#             j = maxHeap.pop()
#             c = c + j._profit
#             k = k - 1
#     return c

def project_selection2(c,k,l):
    while k and l:
        i = len(l) - 1
        while i > -1 and l[i]._cost > c:
            i -= 1
        if i < 0:
            return -1
        c += l[i]._profit
        l.pop(i)
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

