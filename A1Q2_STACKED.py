import sys
import time

""" "Odd move first clockwise"
                                                         = move disk 1 first and whenever i move disk 1, i move in clockwise sequence of ABCABC
"Odd move first counterclockwise"
                                                         = move disk 1 first and whenever i move disk 1, i move in counterclockwise sequence of ACBACB
"Even move first clockwise"
                                                         = DONOT move disk 1 first and whenever i move disk 1, i move in clockwise sequence of ABCABC
"Even move first counterclockwise"
                                                         = DONOT move disk 1 first and whenever i move disk 1, i move in counterclockwise sequence of ACBACB """


def tower_hanoi(disk):
    #matrix = [['x','x','x'] for i in range(8)]
    #print (matrix)
    npeg = ['A','B','C']
    pos = 0
    orig = [l.copy() for l in disk]
    
    for i in range(0,len(disk)):
        if (disk[i] != [] and disk[i][0] == 1):
            pos = i
            break
    n = sum([len(listElem) for listElem in disk])
    list_res = [
        {'type': 'odd clockwise', 'odd': 1, 'clock': 1, 'moves': -99, 'tower': 'Z'},
        {'type': 'even counterclockwise', 'odd': 0, 'clock': -1, 'moves': -99, 'tower': 'Z'},
        {'type': 'odd counterclockwise', 'odd': 1, 'clock': -1, 'moves': -99, 'tower': 'Z'},
        {'type': 'even clockwise', 'odd': 0, 'clock': 1, 'moves': -99, 'tower': 'Z'}
        ]
    
    cur_min = -1
    cur_index = -1
    for i in range(len(list_res)):
        if (list_res[i]['moves'] == -99):
            disk = [l.copy() for l in orig]
            m = tower_hanoi2(n, 0, pos, disk, list_res[i]['odd'], list_res[i]['clock'], orig)
            list_res[i]['moves'] = m
            if (m > -1):
                l = [disk.index(l) for l in disk if len(l) == n]
                list_res[i]['tower'] = npeg[l[0]]
                if (cur_min == -1 or m < cur_min):
                    cur_min = m
                    cur_index = i
    print(list_res)
    #m = tower_hanoi2(n, 0, pos, disk, 0, -1)
    if (cur_index > -1):
        print(list_res[cur_index]['tower'], list_res[cur_index]['moves'], list_res[cur_index]['type'])
    else:
        print('impossible')
    return

def tower_hanoi2(n, moves, pos, disk, oe, clock, orig):
    #base cases
    complete = [k for k in disk if len(k) == n]
    if (complete != []):
        return moves
    elif (orig == disk and moves > 0):
        return -1

    if (oe == 1): # imply ODD
        disk[(pos + clock) % 3].insert(0,disk[pos].pop(0))
        moves = moves + 1
        return tower_hanoi2(n, moves, (pos + clock)%3, disk, (oe+1) % 2, clock, orig)
    if (oe == 0): # implies EVEN
        a = 999 if not disk[(pos + 1) % 3] else disk[(pos + 1) % 3][0]
        b = 999 if not disk[(pos + 2) % 3] else disk[(pos + 2) % 3][0]
        if (a < b):
            disk[(pos + 2) % 3].insert(0,disk[(pos + 1) % 3].pop(0))
        else:
            disk[(pos + 1) % 3].insert(0,disk[(pos + 2) % 3].pop(0))
        moves = moves + 1
        return tower_hanoi2(n, moves, pos, disk, (oe+1) % 2, clock, orig)




""" num_line = int(sys.stdin.readline())
for _ in range(num_line):
    disk = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    print (disk)
    result = tower_hanoi(disk)
    print(result[0], result[1]) """

print(sys.getrecursionlimit())
start_time = time.time()
disk = [[],[1,2,3,5],[4]]
tower_hanoi(disk)
print("--- %s seconds ---" % (time.time() - start_time))
