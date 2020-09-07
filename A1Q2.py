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
    lstMoveCount = []
    pos = 0
    cur_min = -1
    cur_index = -1
    for i in range(0,2):
        if (lstMoves[i]['moves'] == -99):
            #reset parameters
            disk = [l.copy() for l in orig]
            lstMoveCount = []
            pos = getPegIndexOfDiskOne(disk)
            m = tower_hanoi2(pos, disk, lstMoves[i], lstMoveCount)
            #print('# of moves for',lstMoves[i]['type'], 'is', m)
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
            
    #print(cur_index)
    #print(lstMoves)
    if (cur_index == -1):
        print('impossible')
    elif (lstMoves[cur_index]['moves'] == 0):
        print(lstMoves[cur_index]['tower'], lstMoves[cur_index]['moves'])
    else:
        print(lstMoves[cur_index]['tower'], lstMoves[cur_index]['moves'], lstMoves[cur_index]['type'])
    
    return lstMoves

def tower_hanoi2(pos, disk, movObj, lstMoveCount):
    global nDisk,npegs, lstPegs
    #base cases
    complete = [k for k in disk if len(k) == nDisk]
    if (complete != []):
        sumMoves = sum(lstMoveCount)
        movObj['moves'] = sumMoves
        movObj['tower'] = lstPegs[pos]
        #print('Final State', disk)
        return sumMoves
    
    lstContiguousDiskOne = getContiguousDiskOneStack(disk, pos)
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
    # update Disk 1 peg index
    pos = endPosOfDiskOneStack
    # update move count
    lstMoveCount.append(2**lenContiguousDiskOne - 1)

    # compare remaining stacks w/o Disk 1 to initaite move
    a = 999 if not disk[(pos + 1) % npegs] else disk[(pos + 1) % npegs][0]
    b = 999 if not disk[(pos + 2) % npegs] else disk[(pos + 2) % npegs][0]
    if (a < b):
        disk[(pos + 2) % npegs].insert(0,disk[(pos + 1) % npegs].pop(0))
        lstMoveCount.append(1)
    elif (a > b):
        disk[(pos + 1) % npegs].insert(0,disk[(pos + 2) % npegs].pop(0))
        lstMoveCount.append(1)
    
    #print('Before recursing', disk, 'Move array', lstMoveCount)
    return tower_hanoi2(pos, disk, movObj, lstMoveCount)


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

"""
disk = [[19,20,21,24,31],[1,2,3,6,7,8,9,10,11,14,15,16,17,22,25,28,29,30,35],[4,5,12,13,18,23,26,27,32,33,34]]
npegs = len(disk)
#disk = [[1,2,7,8,11,12,15,16,17,22,25,26],[3,14,23,28],[4,5,6,9,10,13,18,19,20,21,24,27]]
#disk = [[19,20,21,24],[1,2,3,6,7,8,9,10,11,14,15,16,17,22,25,28,29,30],[4,5,12,13,18,23,26,27]]
#disk = [[19,20,21,24,31],[1,2,3,6,7,8,9,10,11,14,15,16,17,22,25,28,29,30,35],[4,5,12,13,18,23,26,27,32,33,34]]
#disk = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64],[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62],[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63]]

tower_hanoi(disk)
print("--- %s seconds ---" % (time.time() - start_time))


#1 4, 2 5 8 9, 3 6 7 10
#1,2,7,8,11,12,15,16,17,22,25,26 | 3,14,23,28 | 4,5,6,9,10,13,18,19,20,21,24,27
#19,20,21,24 | 1,2,3,6,7,8,9,10,11,14,15,16,17,22,25,28,29,30 | 4,5,12,13,18,23,26,27
#19,20,21,24,31 | 1,2,3,6,7,8,9,10,11,14,15,16,17,22,25,28,29,30,35 | 4,5,12,13,18,23,26,27,32,33,34
"""