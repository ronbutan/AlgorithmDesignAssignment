from typing import List

matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print(flat)

def twoSum(nums, target):
    l = len(nums)
    index1 = 0
    index2 = 0
    for i in range(l):
        index1 = i
        left = target - nums[i]
        for j in range(i+1,l):
            if nums[j] == left:
                index2 = j
                return [index1,index2]
#print(twoSum([2,7,11,15],9))

def isPalindrome(x):
    s = str(x)
    if len(s) == 2:
        return s[0] == s[1]
    mid = len(s) // 2
    s1 = s[0:mid]
    s2 = s[mid:] if len(s) % 2 == 0 else s[mid+1:]
    return s1 == s2[::-1]
print(isPalindrome("racecar"))

def removeElement(nums, val):
    i = 0
    for x in range(0,len(nums)):
        if nums[x] != val:
            nums[i] = nums[x]
            i += 1
    return nums

def avg(path,sortby = ''):
    with open(path) as file:
        alist = file.read().splitlines() # used to split lines and remove newline character
        lines = [l.split(',') for l in alist]
    d={}
    dname={}
    dfinal = {}
    for i in lines:
        if d.get(i[1], -1) == -1:
            d[i[1]] = [float(i[3])]
            dname[i[1]] = i[0]
        else:
            d[i[1]].append(float(i[3]))
    for k,v in d.items():
        average = sum(v) / len(v)
        dfinal[k] = dname[k],k,average,len(v)
    wlines = [','.join(str(i) for i in tups) for tups in dfinal.values()]
    print(wlines)
    with open('result.txt', 'w') as wfile:
        for i in range(len(wlines)):
            if i + 1 == len(wlines):
                wfile.write(wlines[i])
            else:
                wfile.write(wlines[i] + '\n')

def insertmiddle(s1,s2):
    l = len(s1)
    mid = l//2
    s3 = s1[:mid] + s2 + s1[mid:]
    return s3

def firstmiddlelast(s1,s2):
    s3 = s1[0] + s2[0]
    mid1 = len(s1)//2
    mid2 = len(s2)//2
    print(mid1)
    s3 = s3 + s1[mid1] + s2[mid2] + s1[-1] + s2[-1]
    return s3

def lowercasefirst(s1):
    upper = []
    lower = []
    for c in s1:
        if c.islower():
            lower.append(c)
        else:
            upper.append(c)
    return ''.join(lower + upper)

def countchardigitsymbol(s1):
    upper = 0
    lower = 0
    dig = 0
    symbol = 0
    for c in s1:
        if c.isalpha():
            if c.islower():
                lower += 1
            else:
                upper += 1
        elif c.isdigit():
            dig += 1
        else:
            symbol += 1
    return upper,lower,dig,symbol

def createmixedstring(s1,s2):
    smallest = min([len(s1),len(s2)])
    s3 = s2[::-1]
    s4=''
    r = 2
    if len(s1) <= len(s2):
        r = 1
    for i in range(smallest):
        s4 = s4 + s1[i] + s3[i]
    if r == 1:
        s4 = s4 + s2[i+1:]
    else:
        s4 = s4 + s1[i+1:]
    return s4

def balancestring(s1,s2):
    l2 = [i for i in s1 if i not in s2]
    return l2 == []

def findnumoccurence(s1,s2):
    s2 = s2.lower()
    s1 = s1.lower()
    pointer = 0
    num = 0
    while 1:
        pointer = s2.find(s1,pointer,len(s2))
        if pointer > -1:
            num += 1
            pointer += len(s1)
        else:
            break
    return num

'''
get length of a number without converting to string
'''
# n = 785670
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1
# print(count)

'''
reverse number without converting to string.
'''
# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revered Number ", reverse_number)

'''
Reverse number pattern
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
def reversenumberpattern(n):
    l = []
    nums = []
    for i in range(1,n+1):
        j = 1
        nums = []
        while j < (i+1):
            nums.append(str(j))
            j += 1
        s = " ".join(nums)
        l.append(s)
    return "\n".join([s[::-1] for s in l])

def evenpyramid(n):
    j = 0
    l = []
    for i in range(0,n+1,2):
        s = ''
        s = s + str(i) + str(i*2) * j
        j += 1
        l.append(s)
    return l


'''
Half pyramid pattern with numbers
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
def halfpyramidwithnumbers(n):
    for i in range(1, n+1):
        for column in range(1, i + 1):
            print(column, end=' ')
        print("")

'''
Inverted Pyramid pattern with numbers
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
def invertedpyramid(n):
    b = 1
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(b, end=' ')
        b += 1
        print('\r')

'''
Display descending order of number
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
'''
def descendingorder(n):
    for i in range(n,0,-1):
        for j in range(1,i + 1):
            print(i, end=' ')
        print("")

'''
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
'''
def invertedpyramiddesc(n):
    for i in range(n, 0, -1):
        for j in range(0, i + 1):
            print(j, end=' ')
        print("\r")

'''
Double the number
1 
2    1 
4    2    1 
8    4    2    1 
16    8    4    2    1 
32   16    8    4    2    1 
64   32   16    8    4    2    1 
128   64   32   16    8    4    2    1
'''
def doublenumberpyramid(n):
    for i in range(1, n):
        for j in range(-1+i, -1, -1):
            print(format(2**j, "4d"), end=' ')
        print("")

'''
1 
1    2    1 
1    2    4    2   1 
1    2    4    8   4    2    1 
1    2    4    8   16   8    4   2    1 
1    2    4    8   16   32   16  8    4    2    1 
1    2    4    8   16   32   64  32   16   8    4    2    1 
1    2    4    8   16   32   64  128  64   32   16   8    4    2    1
'''

def pattern9(n):
    for i in range(1, n):
        for i in range(0, i, 1):
            print(format(2 ** i, "4d"), end=' ')
        for i in range(-1 + i, -1, -1):
            print(format(2 ** i, "4d"), end=' ')
        print("")

'''
Even number pattern
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
'''
def evenpattern(rows):
    LastEvenNumber = 2 * rows
    evenNumber = LastEvenNumber
    for i in range(1, rows+1):
        evenNumber = LastEvenNumber
        for j in range(i):
            print(evenNumber, end=' ')
            evenNumber -= 2
        print("\r")

'''
Display men’s pant style pattern with numbers
5 4 3 2 1 1 2 3 4 5 

5 4 3 2     2 3 4 5 

5 4 3         3 4 5 

5 4             4 5 

5                 5
'''
def menspants(n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            print(j, '', end='')
        for l in range(i):
            print('    ', end='')
        for k in range(i + 1, n):
            print(k, '', end='')
        print('\n')

'''
Alternate number
'''
def altnumber(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print((i * 2 - 1), end=" ")
            j = j + 1
        i = i + 1
        print()
'''
Square pattern
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
'''
def squarepattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j <= i:
                print(i, end=' ')
            else:
                print(j, end=' ')
        print()
'''
Right-angled triangle pattern with numbers
        1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5
'''
def rightangletriangle(rows):
    for row in range(1, rows):
        num = 1
        for j in range(rows, 0, -1):
            if j > row:
                print(" ", end=' ')
            else:
                print(num, end=' ')
                num += 1
        print("")

'''
Pascal’s Triangle Pattern using numbers
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
'''
def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()

def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

'''
star triangle
            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  *
'''
def startriangle():
    size = 7
    m = (2 * size) - 2
    for i in range(0, size):
        for j in range(0, m):
            print(end=" ")
        m = m - 1  # decrementing m after each loop
        for j in range(0, i + 1):
            # printing full Triangle pyramid using stars
            print("* ", end=' ')
        print(" ")
'''
Left half pyramid
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
def lefthalfpyramid():
    rows = 5
    k = 2 * rows - 2
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
'''
Inverted star pyramid
* * * * *  
* * * *  
* * *  
* *  
*
'''
def invertedstarpyramid():
    rows = 5
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
'''
Print Right start Pattern with Star (asterisk)
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
def rightstartpattern():
    rows = 5
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")
'''
Downward star pattern
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
'''
def downwardstarpattern():
    rows = 5
    k = 2 * rows - 2
    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")
'''
2 pyramid
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
'''
def twopyramid():
    rows = 6
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print(" ")

    print(" ")

    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
'''
Diamond Shaped
     * 
     * * 
    * * * 
   * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
'''
def diamondshape():
    rows = 5
    k = 2 * rows - 2
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
        
    k = rows - 2

    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
'''
Display men's pants pattern
****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
'''
def menspantspatternstar():
    rows = 14
    print("*" * rows, end="\n")
    i = (rows // 2) - 1
    j = 2
    while i != 0:
        while j <= (rows - 2):
            print("*" * i, end="")
            print("_" * j, end="")
            print("*" * i, end="\n")
            i = i - 1
            j = j + 2
'''
Right triangle alphabet
A  
B C  
D E F  
G H I J  
K L M N O  
P Q R S T U  
V W X Y Z [ \
'''
def righttrianglealpha():
    asciiNumber = 65
    for i in range(0, 7):
        for j in range(0, i + 1):
            character = chr(asciiNumber)
            print(character, end=' ')
            asciiNumber += 1
        print(" ")
'''
Equilateral triangle alphabets
           A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \  
'''
def equilateraltrianglealphabets():
    size = 7
    asciiNumber = 65
    m = (2 * size) - 2
    for i in range(0, size):
        for j in range(0, m):
            print(end=" ")
        m = m - 1
        for j in range(0, i + 1):
            character = chr(asciiNumber)
            print(character, end=' ')
            asciiNumber += 1
        print(" ")
# def addlist(*l):
#     l3 = [[ l1[i][j] + l2[i][j] for j in range(len(l1[i]))] for i in range(len(l1))]
#     a = zip(*l)
    
#     return l3

number_list = [4,5,6]
str_list = [1,2,3]
# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_set = set(result)
print(result_set)
#print(addlist([[1, -2, 3], [-4, 5, -6], [7, -8, 9]],[[1, 1, 0], [1, -2, 3], [-2, 2, -2]]))

def sky_diff(M):
    n = len(M)
    #compute matrix with column values
    l4 = [[M[j][i] for j in range(n)] for i in range(len(M[0]))]
    minlist = [[min(l)] for l in l4]
    maxlist = [[max(l)] for l in M]
    for i in range(n):
        for j in range(len(M[i])):
            M[i][j] = maxlist[i][0] - minlist[j][0]
    print(M)
sky_diff([[4,1,8],[5,2,5],[9,7,1]])
#sky_diff([[2,2],[2,2]])

s = list(map(int,['1','3']))
s1 = set('RON')

# def longestCommonPrefix(self, strs: List[str]) -> str:
#     n = len(strs)
#     lenlst = [len(s) for s in strs]
#     smallest = min(lenlst)
#     minindices = [i for i,x in enumerate(strs) if len(x) == smallest]
#     validPrefix = []
#     isPass = True
#     for short in range(len(minindices)):
#         prefix = strs[minindices[short]]
#         idx = len(prefix) - 1
#         while idx > -1:
#             if idx == 0:
#                 prefix_ = prefix[0]
#             else:
#                 prefix_ = prefix[0:idx+1]
#             for j in range(n):
#                 if j == minindices[short]:
#                     continue
                
#                 s = strs[j]
#                 if idx == 0 and s[0] == prefix_:
#                     continue
#                 elif idx > 0 and s[0:idx+1] == prefix_:
#                     continue
#                 else
#                     isPass = False
#                     break
#             if isPass:
#                 validPrefix.append(prefix_)
#             idx -= 1

def printSinWave(wave_height, wave_length): 
  
    # inner space and outer space. 
    Is = 1
    os = 2
  
    # for loop for height of wave 
    for i in range(1, wave_height + 1): 
  
        # for loop for wave length 
        for j in range(1, wave_length + 1): 
  
            # intermediate spaces 
            for k in range(1, os + 1): 
                print(end = " ") 
              
            # put any symbol 
            print("0", end = "") 
  
            for k in range(1, Is + 1):  
                print(end = " ")          
  
            # put any symbol 
            print("0", end = "") 
  
            for k in range(1, os + 1): 
                print(end = " ") 
              
            print(end = " ") 
          
        # set a value of os to 1 if i+1 Is not  
        # equal to wave height or 0 otherwise 
        if (i + 1 != wave_height): 
            os = 1
        else: 
            os = 0
              
        # set value of Is to 3 if i+1 Is not  
        # equal to wave height or 5 otherwise 
        if (i + 1 != wave_height): 
            Is = 3
        else: 
            Is = 5
        print()  
  
# Driver code 
wave_height, wave_length = 5, 10
printSinWave(wave_height, wave_length) 
  
# This code is contributed by  
# Mohit kumar 29 

# Python3 implementation to print 
# reverse wave form of matrix 
# function to print reverse wave  
# form for a given matrix 
def wavePrint(m, n, arr): 
    j = n - 1
    wave = 1
      
    # m     - Ending row index 
    # n     - Ending column index 
    # i, j     - Iterator 
    # wave     - for Direction 
    # wave = 1 - Wave direction down 
    # wave = 0 - Wave direction up  
    while j >= 0: 
          
        # Check whether to go in 
        # upward or downward 
        if wave == 1: 
      
            # Print the element of the  
            # matrix downward since the 
                        # value of wave = 1 
            for i in range(m): 
                print(arr[i][j], end = " "), 
            wave = 0
            j -= 1
              
              
        else: 
            # Print the elements of the  
            # matrix upward since the  
            # value of wave = 0 
            for i in range(m - 1, -1, -1): 
                print(arr[i][j], end = " "), 
                  
            wave = 1
            j -= 1
  
# Driver code 
arr = [ [ 1, 2, 3, 4 ], 
        [ 5, 6, 7, 8 ], 
        [ 9, 10, 11, 12 ], 
        [ 13, 14, 15, 16 ] ] 
R = 4
C = 4
wavePrint(R, C, arr) 
  
# This code is contributed by  
# Upendra Singh Bartwal 
# print array in Z form
# Python program to print a  
# square matrix in Z form 
def Zform():
    arr = [[4, 5, 6, 8],  
            [1, 2, 3, 1],  
            [7, 8, 9, 4],  
            [1, 8, 7, 5]] 
    
    n = len(arr[0]) 
                    
    i = 0
    for j in range(0, n-1): 
        print(arr[i][j], end = ' ')  
            
    k = 1
    for i in range(0, n): 
        for j in range(n, 0, -1): 
            if(j == n-k): 
                print(arr[i][j], end = ' ')  
                break;  
        k+= 1
    
    # Print last row 
    i = n-1;  
    for j in range(0, n): 
        print(arr[i][j], end = ' ') 

# Python 3 program to print 
# matrix in zig-zag form 
  
# Method to print matrix  
# in zig-zag form 
def printZigZag(row, col, a): 
    evenRow = 0 # starts from the first row 
    oddRow = 1 # starts from the next row 
  
    while evenRow < row:  
        for i in range(col): 
              
            # evenRow will be printed 
            # in the same direction 
            print(str(a[evenRow][i] ),  
                           end = " ") 
                             
        # Skipping next row so as 
        # to get the next evenRow 
        evenRow = evenRow + 2
              
        if oddRow < row: 
            for i in range(col - 1, -1, -1): 
                  
                # oddRow will be printed in 
                # the opposite direction 
                print(str(a[oddRow][i]),  
                             end = " ") 
                  
        # Skipping next row so as  
        # to get the next oddRow 
        oddRow = oddRow + 2
  
# Driver Code  
r = 3
c = 5
  
mat = [[1, 2, 3, 4, 5], 
       [6, 7, 8, 9, 10], 
       [11, 12, 13, 14, 15]]; 
  
printZigZag(r , c , mat) 
  
# This code is contributed  
# by ChitraNayal 

# Python3 Code to Print a given   
# matrix in reverse spiral form 
  
# This is a modified code of 
# https:#www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/ 
  
def ReversespiralPrint(m, n, a): 
  
    # Large array to initialize it 
    # with elements of matrix 
    b = [0 for i in range(100)] 
  
    #/* k - starting row index 
    #l - starting column index*/ 
    i, k, l = 0, 0, 0
  
    # Counter for single dimension array 
    # in which elements will be stored 
    z = 0
  
    # Total elements in matrix 
    size = m * n 
  
    while (k < m and l < n): 
          
        # Variable to store value of matrix. 
        val = 0
  
        # Print the first row  
        # from the remaining rows  
        for i in range(l, n): 
              
            # printf("%d ", a[k][i]) 
            val = a[k][i] 
            b[z] = val 
            z += 1
        k += 1
  
        # Print the last column 
        # from the remaining columns 
        for i in range(k, m): 
  
            # printf("%d ", a[i][n-1]) 
            val = a[i][n - 1] 
            b[z] = val 
            z += 1
  
        n -= 1
  
        # Print the last row  
        # from the remaining rows 
        if (k < m): 
            for i in range(n - 1, l - 1, -1): 
                  
                # printf("%d ", a[m-1][i]) 
                val = a[m - 1][i] 
                b[z] = val 
                z += 1
  
        m -= 1
  
        # Print the first column  
        # from the remaining columns  
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                  
                # printf("%d ", a[i][l]) 
                val = a[i][l] 
                b[z] = val 
                z += 1
            l += 1
  
    for i in range(size - 1, -1, -1): 
        print(b[i], end = " ") 
  
# Driver Code
R, C = 3, 6
a = [[1, 2, 3, 4, 5, 6], 
     [7, 8, 9, 10, 11, 12], 
     [13, 14, 15, 16, 17, 18]] 
  
ReversespiralPrint(R, C, a) 
  
# This code is contributed by mohit kumar 


def spiralOrder(matrix):
    if not matrix:
        return matrix
    
    aux = []
    rLen = len(matrix)
    cLen = len(matrix[0])
    left = 0
    right = cLen - 1
    up = 0
    down = rLen - 1
    while left <= right and up <= down:
        aux.extend([i for i in matrix[up][left:right+1]])
        if up < down:
            aux.extend([i[right] for i in matrix[up+1:down]])
        if left <= right and up < down:
            aux.extend([i for i in matrix[down][left:right+1][::-1]])
        if up < down and left < right:
            aux.extend([i[left] for i in matrix[up+1:down][::-1]])
        right = right - 1
        left = left + 1
        up = up + 1
        down = down - 1
        print(aux)

mat = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

#mat = [[3],[2]]
# mat = [
#     [7],
#     [9],
#     [6]
# ]
# mat = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
spiralOrder(mat)

l = [[str(i) + str(j) for i in range(3)] for j in range(2)]
print(l)
l1 = [str(i) + str(j) for i in range(4) for j in range(2)]
print(l1)

s = 'rona'
for i in range(-1,-len(s) - 1,-1):
    print(s[i])

n = 8000
while(n > 0):
    digit = n % 10
    n = n // 10
    print(digit, n)

l = [12,13,14]
print("".join(map(str,l)))



def _print(arr: list, size: int): 
    for i in range(size): 
        print(arr[i], end=" ") 
