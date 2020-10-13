import sys
import time

def LCMS(a, b):
    lenA = len(a)
    lenB = len(b)
    # find Longest Common Subsequence between A and B
    storageMatrix = [[0 for i in range(lenB + 1)] for j in range(lenA + 1)]
    larger = float("-inf")
    for row in range(1, lenA+1):
        for col in range(1, lenB+1):
            if a[row - 1] == b[col - 1]:
                storageMatrix[row][col] = storageMatrix[row-1][col-1] + 1
            else:
                larger = max(storageMatrix[row-1][col], storageMatrix[row][col-1])
                storageMatrix[row][col] = larger
    row = lenA
    col = lenB
    dummy = []
    while row > 0 and col > 0:
        if a[row-1] == b[col-1]:
            dummy.insert(0, b[col-1].zfill(4))
            col-=1
            row-=1
        else:
            if storageMatrix[row][col-1] >= storageMatrix[row-1][col]:
                col-=1
            else:
                row-=1
    
    #dummy = [int(n,16) for n in dummy]
    lenLongest = 0
    # list of 1 element is also mountain of length 1, there minimum increasing sequence is 1
    lstIncr = [1 for n in dummy]
    lstDecr = [1 for n in dummy]
    for i in range(1, len(dummy)):
        for j in range(0,i):
            # length of sequence at back must be larger or equal than length in front
            if dummy[i] > dummy[j]:
                lstIncr[i] = max(lstIncr[i], lstIncr[j] + 1)
    
    
    for i in range(len(dummy)-2, -1,-1):
        for j in range(len(dummy)-1,i,-1):
            # length of sequence at back must be larger or equal than length in front
            if dummy[i] > dummy[j]:
                lstDecr[i] = max(lstDecr[i], lstDecr[j] + 1)


    for i in range(0, len(dummy)):
        lenLongest = max(lstIncr[i] + lstDecr[i] - 1, lenLongest)
    return lenLongest if lenLongest <= 1000 else 1000

num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = sys.stdin.readline().split()
    b = sys.stdin.readline().split()
    if not a or not b:
        print("0")
        continue
    testa = [c for c in a if len(c) > 4]
    testb = [c for c in b if len(c) > 4]
    if testa or testb:
        print("0")
        continue
    #startTime = time.time()
    print(LCMS(a, b))
    #print('---- %.6g seconds ----' % (time.time() - startTime))
