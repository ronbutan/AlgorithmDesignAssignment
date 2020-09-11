import sys
import time

def initParams(disk):
    global nDisk,maxMoves,npegs,oe
    npegs = len(disk)
    nDisk = getNumOfDisk(disk)
    maxMoves = 2**nDisk - 1
    oe = nDisk % 2

def getNumOfDisk(disk):
    return sum([len(k) for k in disk])

def getPegIndexOfDiskOne(disk):
    # determine peg placement of Disk 1
    pos = -99
    for i in range(0,len(disk)):
        if (disk[i] != [] and disk[i][0] == 1):
            pos = i
            break
    return pos

def getContiguousDiskOneStack(disk, pos):
    l = disk[pos]
    no = len(l)
    if (no == 1):
        return disk[pos].copy()
    end = 1
    for i in range(no):
        if (end < no and l[i] + 1 == l[end]):
            end += 1
        else:
            break
    return l[0:end]

def tower_hanoi(disk):
    orig = [l.copy() for l in disk]
    global maxMoves, oe, npegs
    lstMoves = [
        {'type': 'odd clockwise', 'odd': 1, 'clock': 1, 'moves': -99, 'tower': 'Z', 'postoendonodd': 1,'postoendoneven': 2, 'mirror': 2},
        {'type': 'odd counterclockwise', 'odd': 1, 'clock': -1, 'moves': -99, 'tower': 'Z', 'postoendonodd': 2,'postoendoneven': 1, 'mirror':2},
        {'type': 'even counterclockwise', 'odd': 0, 'clock': -1, 'moves': -99, 'tower': 'Z', 'postoendonodd': 2,'postoendoneven': 1, 'mirror':-2},
        {'type': 'even clockwise', 'odd': 0, 'clock': 1, 'moves': -99, 'tower': 'Z', 'postoendonodd': 1,'postoendoneven': 2,'mirror':-2},
        ]
    pos = 0
    cur_min = -1
    cur_index = -1
    for i in range(0,2):
        if (lstMoves[i]['moves'] == -99):
            #reset parameters
            disk = [l.copy() for l in orig]
            pos = getPegIndexOfDiskOne(disk)

            # start recursion
            m = tower_hanoi2(pos, disk, lstMoves[i], 0)
            obj = lstMoves[i + lstMoves[i]['mirror']]
            if (m > -1 and (cur_min == -1 or m < cur_min)):
                    cur_min = m
                    cur_index = i
            if (m == -1): # imply IMPOSSIBLE
                # update mirror
                obj['moves'] = m
            else:
                remainingMoves = maxMoves - m
                obj['moves'] = remainingMoves
                if (oe == 1):
                    endpos = (getPegIndexOfDiskOne(disk) + obj['postoendonodd']) % npegs
                else:
                    endpos = (getPegIndexOfDiskOne(disk) + obj['postoendoneven']) % npegs
                obj['tower'] = lstPegs[endpos]
                if (cur_min == -1 or remainingMoves < cur_min):
                    cur_min = remainingMoves
                    cur_index = i + lstMoves[i]['mirror']
            
    if (cur_index == -1):
        print('impossible')
    elif (lstMoves[cur_index]['moves'] == 0):
        print(lstMoves[cur_index]['tower'], lstMoves[cur_index]['moves'])
    else:
        print(lstMoves[cur_index]['tower'], lstMoves[cur_index]['moves'], lstMoves[cur_index]['type'])
    
    return lstMoves

def tower_hanoi2(pos, disk, movObj, moves):
    global nDisk,npegs, lstPegs
    #base cases
    if (len(disk[pos]) == nDisk):
        movObj['moves'] = moves
        movObj['tower'] = lstPegs[pos]
        return moves
    
    lstContiguousDiskOne = getContiguousDiskOneStack(disk, pos) # n
    lenContiguousDiskOne = len(lstContiguousDiskOne)
    endPosOfDiskOneStack = -1
    maxDiskNo = lstContiguousDiskOne[-1]
    if (lenContiguousDiskOne % 2 == 1):
        endPosOfDiskOneStack = (pos + movObj['postoendonodd']) % npegs
    else:
        endPosOfDiskOneStack = (pos + movObj['postoendoneven']) % npegs
    
    # check for illegal move
    if (disk[endPosOfDiskOneStack] == [] or (maxDiskNo + 1) != disk[endPosOfDiskOneStack][0]):
        movObj['moves'] = -1
        return -1

    # move contiguous stack to destination stack
    disk[endPosOfDiskOneStack] = lstContiguousDiskOne + disk[endPosOfDiskOneStack]
    # update source stack to remove contiguous stack
    disk[pos] = disk[pos][lenContiguousDiskOne:]
    # update peg index of peg having Disk 1
    pos = endPosOfDiskOneStack
    # update move count
    moves = moves + 2**lenContiguousDiskOne - 1
    #lstMoveCount.append(2**lenContiguousDiskOne - 1)

    # compare remaining stacks w/o Disk 1 to initiate move
    a = 999 if not disk[(pos + 1) % npegs] else disk[(pos + 1) % npegs][0]
    b = 999 if not disk[(pos + 2) % npegs] else disk[(pos + 2) % npegs][0]
    if (a < b):
        disk[(pos + 2) % npegs].insert(0,disk[(pos + 1) % npegs].pop(0))
        moves = moves + 1
    elif (a > b):
        disk[(pos + 1) % npegs].insert(0,disk[(pos + 2) % npegs].pop(0))
        moves = moves + 1
    
    return tower_hanoi2(pos, disk, movObj, moves)


nDisk = 0
maxMoves = 0
lstPegs = ['A','B','C']
npegs = 0
oe = 0
num_line = int(sys.stdin.readline())
for _ in range(num_line):
    disk = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    initParams(disk)
    #start_time = time.time()
    result = tower_hanoi(disk)
    #print(result) 
    #print("--- %s seconds ---" % (time.time() - start_time)) 

'''
Analysis:

n for loop to determine contigous stack with Disk 1
T(n - 1) for recursive call to itself
constants are not considered due to lower order


T(n) = 1, when n = 0
T(n) = T(n-1) + n, when n > 0

T(0) = 1 (base case)

T(n) = T(n-1) + n ------------------ (1)
T(n-1) = T(n-2) + (n-1)
T(n-2) = T(n-3) + (n-2)


T(n) = T(n-2) + (n-1) + n ---------- (2)
T(n) = T(n-3) + (n-2) + (n-1) + n -- (3)

Do k times,

T(n) = T(n-k) + (n-(k-1)) + (n-(k-2)) + ... + (n-1) + n ----- (4)

Assume continuation to T(0) where n-k = 0 ==> n = k,
T(n) = T(n-n) + (n-(n-1) + (n-(n-2)) + ... + (n-1) + n
T(n) = T(0) + 1 + 2 + ... + (n-1) + n
T(n) = 1 + 1 + 2 + ... + (n-1) + n
T(n) = 1 + (n(n-1)/2)
T(n) = O(n**2)

'''