from typing import List
x = sum([i if i%2==0 else 1 for i in range(20)])
print(x)

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
        s = s + str(i) + (i*2) * j
        j += 1
        l.append(s)
    print(l)

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

s = 'Snake'
s1 = s
s1 = s1 + 'n'
print(s, s1)

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
  
  
# Function to construct and print Longest 
# Bitonic Subsequence 
def printLBS(arr: list, n: int): 
  
    # LIS[i] stores the length of the longest 
    # increasing subsequence ending with arr[i] 
    LIS = [0] * n 
    for i in range(n): 
        LIS[i] = [] 
  
    # initialize LIS[0] to arr[0] 
    LIS[0].append(arr[0]) 
  
    # Compute LIS values from left to right 
    for i in range(1, n): 
  
        # for every j less than i 
        for j in range(i): 
  
            if ((arr[j] < arr[i]) and (len(LIS[j]) > len(LIS[i]))): 
                LIS[i] = LIS[j].copy() 
  
        LIS[i].append(arr[i]) 
  
    # LIS[i] now stores Maximum Increasing 
    # Subsequence of arr[0..i] that ends with 
    # arr[i] 
  
    # LDS[i] stores the length of the longest 
    # decreasing subsequence starting with arr[i] 
    LDS = [0] * n 
    for i in range(n): 
        LDS[i] = [] 
  
    # initialize LDS[n-1] to arr[n-1] 
    LDS[n - 1].append(arr[n - 1]) 
  
    # Compute LDS values from right to left 
    for i in range(n - 2, -1, -1): 
  
        # for every j greater than i 
        for j in range(n - 1, i, -1): 
  
            if ((arr[j] < arr[i]) and (len(LDS[j]) > len(LDS[i]))): 
                LDS[i] = LDS[j].copy() 
  
        LDS[i].append(arr[i]) 
  
    # reverse as vector as we're inserting at end 
    for i in range(n): 
        LDS[i] = list(reversed(LDS[i])) 
  
    # LDS[i] now stores Maximum Decreasing Subsequence 
    # of arr[i..n] that starts with arr[i] 
  
    max = 0
    maxIndex = -1
  
    for i in range(n): 
  
        # Find maximum value of size of LIS[i] + size 
        # of LDS[i] - 1 
        if (len(LIS[i]) + len(LDS[i]) - 1 > max): 
  
            max = len(LIS[i]) + len(LDS[i]) - 1
            maxIndex = i 
  
    # print all but last element of LIS[maxIndex] vector 
    _print(LIS[maxIndex], len(LIS[maxIndex]) - 1) 
  
    # print all elements of LDS[maxIndex] vector 
    _print(LDS[maxIndex], len(LDS[maxIndex])) 
  
 
# Driver program to test the above function 
dummy = ['04f2', '40c7', '058e', '1a99', '067d', 'e17a', '0bad', '4a88', '1218', '9363', '1ac4', 'a210', '1b8a', '542e', '2479', '5a63', '2a51', '6a75', '2b37', '41c2', '2ee3', '6c2b', '37cc', 'de82', '43e8', '83d5', '48c2', '7338', 
'4cb0', '7a46', '512a', 'ba69', '631f', 'ab46', '6466', '941d', '71af', '9f66', '75e1', 'a5cf', '7c8c', 'd6ca', '7e95', 'ea8e', '7eef', 'e916', '8003', '8f75', '89c8', '993d', '9083', 'e367', '92fc', '9721', '93b3', 'd39f', 'a30f', 'c647', 'a3ab', 'e446', 'aaac', 'f6e5', 'b84f', 'baba', 'b8ff', 'bc49', 'b9c3', 'c285', 'c232', 'fefc', 'c604', 'de44', 'c6f5', 'f7f0', 'cc17', 'd548', 'd46c', 'ea89', 'd6b6', 'fa5c', 'd77a', 'ed83', 'e067', 'ef7c', 'e219', 'fb39', 'e7ed', 'f65b', 'e9ef', 'f515', 'f11f', 'f92c', 'f290', 'fdb1', 'f387', 'ff08', 'fc42', 'ff7f', 'ff68', 'aa83', 'ff2c', '61e1', 'ff27', '2263', 'fd15', '70aa', 'f69c', '34f8', 'f213', '95f0', 'f20b', 'eb28', 'ed6c', '9965', 'ec99', 'de21', 'e3ee', 'd0af', 'e19a', '28d7', 'dc8c', 'a42f', 'd781', 'b9fb', 'd14d', 'bf4b', 'cf1a', '4eeb', 'cbf6', '8fe5', 'c471', '1313', 'c2af', 'bda0', 'bff7', '4f16', 'bdaa', '1b4f', 'b645', '10bc', 'b4e3', '8d96', 'b447', '5e05', 'b2e9', '878c', 'b241', '6f5e', '9b9e', '1d51', '8bc6', '1efb', '81ef', '75f3', '7fdf', '2484', '743a', '2581', '6a93', '1498', '66c0', '53dd', '6464', '22b3', '5ac5', '56a6', '597f', '3b5a', '554c', '2b49', '5229', '02c9', '4e7c', '1091', '4067', '0351', 'afe4', '3643', '3b2d', '1797', '2af7', '0db5', '293f', '0af0', '1878', '0ffb', '154c', '1083', '123d', '0a86', '122b', '0196', '10b5', '0275', '0462', '0161', '0419']
dummy = [10,10,22,9,33,21,50,41,60,80,1]
printLBS(dummy,len(dummy))

def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 

a = ['4d17', 'b610', '2349', 'a966', '8b57', '11a', '4f2', '3a05', '6734', 'd741', '40c7', 'a5f1', '2fc0', '58e', '6127', 'ba28', '2cce', '495b', '23bc', '1a99', '17ac', '67d', '6d87', 'a0f3', 'e17a', '1949', 'e7af', '3eb6', 'bad', '5d13', 'dfb', 'e63b', '4a88', 'c217', '70a', 'b844', '1218', 'c587', '9e04', '9363', 'a6e1', '9479', 'c98b', 'f07b', '1ac4', 'fdc1', 'ff27', 'd31f', '85f5', '56bf', 'a931', '6f29', 'a210', '6482', 'ca6', '3faf', '1b8a', 'd520', '542e', '9f2', 'f416', 'b83a', '2479', 'cc2c', 'e2a2', '2c5d', '5a63', '9b19', '90c5', '32bd', '2a51', '4e21', '6a75', 'bf29', 'f5b1', 'e11b', '2b37', '1ef3', '41c2', '5def', '931a', 'db43', 'cc6d', 'c02', '4f09', '2ceb', 'bc60', 'cd1e', '2ee3', 'e5cc', '6c51', '6eed', '6c2b', '8b45', '37c', '37cc', '8506', 'de82', '15fb', '4960', '96b', '43e8', '5787', 'c23', 'f952', '83d5', '4902', '66a9', '919', '48c2', '2266', 'f729', 'f537', 'df7', '7338', 'ff61', '4cb0', '2e34', '824c', '7a46', '9cd9', '2a7a', '7a6e', 'eafa', 'b2fc', '512a', '8145', 'ce2e', '7ad5', '6a43', 'ba69', '17c2', '631f', '3ebb', '57f8', '9b61', 'd61a', 'e006', 'ccd1', 'ab46', 'c133', 'ae0', '6466', '9d65', '941d', 'e9e1', '18f3', '681b', '71af', 'ae60', '4593', '9f66', '9f4a', '664', '1478', '80f5', '5cbc', '75e1', '4fc3', 'd0ac', 'e603', 'a5cf', '790e', '8cdc', '7c8c', 'b1bf', 'd0bb', '1249', 'd6ca', 'b330', '4719', '7e95', 'b798', '8e96', '2fa', 'ea8e', '7c09', '5dc8', 'e44d', '7eef', '2916', 'c560', '8a5', '901e', '3bb3', 'e916', 'c4fa', '4853', '1fd5', '8003', 'd9a4', '54c2', 'c749', '8f75', 'c638', '1c6', 'ad61', '89c8', '924d', '51e4', '993d', '72c5', '9083', 'b784', 'e367', '1bb6', 'f117', '92fc', '1a6', '29b4', '79e6', '9cef', '9721', 'c05', 'a160', '6009', '96b9', '93b3', '4c3a', 'd39f', '84b3', 'a30f', 'd3ba', '710e', '65d', 'c647', '2c64', 'd492', '19ba', '5902', '3b4e', 'a3ab', 'd81c', 'e446', '3373', '4dc1', '5b75', 'aaac', '5610', 'a10a', 'f6e5', '4b70', 'd9fe', 'fe58', '73cf', 'a9cb', 'dfca', '9d4', 'b84f', 'b6af', '994b', '23bc', 'baba', 'b3af', '1469', 'b8ff', 
'2da0', '53b0', '2a6e', 'f4e4', 'bc49', '7813', '4c92', 'b9c3', 'dd', 'fdda', 'c285', 'f736', 'f184', 'f446', '7104', 'c232', '574c', '7708', '99a2', 'fefc', 'ddba', '13e7', '8632', '2bd6', 'c604', '1d94', '62c6', 'de44', '8ad0', 'd249', '70d1', '1aae', 'eaf8', 'c6f5', 'db35', '417c', '8036', '8f23', '7cf5', '6782', 'f7f0', '29a0', 'cc17', 'd219', '9fe0', '2595', '5d97', 'd548', 'd165', 'f090', 'd46c', '982f', '9050', 'c139', 'e1ab', 'ea89', '9c58', 'cd97', 'a022', '55dc', '25b7', 'd6b6', '7634', '7ec6', '840a', 'fa5c', '50fe', 'c0b8', '7caa', 'cd1', 'd77a', '2406', '1f16', 'b828', 'ed83', 'c8af', 'eaac', 'e067', 'dccb', 'd749', 'd939', 'ef7c', '33c5', '1037', 'f827', 'e219', 'a347', 'e0ff', 'a9a1', '4588', 'fb39', 'd54c', '78a1', 'bb9a', 'e7ed', 'f4b', '8760', '4a4f', 'f65b', '1dca', 'e9ef', 'ea43', '69bc', 'e51e', 'f515', 'cc64', '527a', 'f11f', '41ba', '6750', 'cf3e', 'f92c', '2a50', 
'f290', 'a8a8', '7e0d', 'fdb1', '7037', '1e19', 'dad', 'bea3', 'f387', '552f', 'ff08', 'b0ec', 'f250', 'fc42', '516c', '44ca', 'def', 'ff7f', '37d0', '5b4a', 'a784', '55f4', '7be6', '49b3', '9f9f', 'ff68', '996b', 'cc9d', '2098', 'f297', '422b', 'aa83', '877d', 'b750', 'ff2c', 'ca6c', '7b38', '61e1', 'abda', '75f', '886e', '68e4', 'ff27', '4dc5', '609d', 'c863', '2263', '2cfd', '49ce', '7c36', 'fd15', 'bc57', '2d2d', 'ed90', '70aa', 'b789', 'c8c8', '5d33', 'f69c', 'a442', '20b3', '8a2c', '4cf5', '34f8', '5543', 'bdcd', 'd049', '764d', 'f213', 'd0e3', '4bc6', 'c49f', '95f0', 'f46b', 'cce6', '1c7', 'c1e0', 'f20b', '21b1', 'de94', 'de60', '5b05', '3f9a', 'eb28', 'b86f', 'c688', '4063', 'b8', 'ed6c', '50ad', '79e1', 'c91a', '302d', '77a4', '6285', '9965', 'ced4', '81e1', 'd666', '140f', 'f4a0', 'ec99', 'd338', 'd3fb', 'de21', '5cca', '8411', 'e3ee', '9ad8', 'd0af', '74c0', 'ff4', 'be9d', 'c663', 'e19a', '8e61', 'e362', '28d7', 'c05b', 'fc30', 'dc8c', '7a0c', 'e0e4', 'c844', '3943', '76ea', 'a42f', 'f301', 'd781', 'b68c', 'a686', '744d', 'ce12', '5126', 'd9f5', 'b9fb', '32b7', 'cb7a', '9ee2', 'd14d', '9cbb', 'e918', 'ae5d', 'bf4b', '28a1', 'ebd6', 'cf1a', 'a1bc', 'deda', '4eeb', '1d82', 'a3b6', '199d', 'ca9e', '2ec6', 'cbf6', 'cc37', '6943', '31e9', '8fe5', '965c', '3393', 'c471', 'a33d', '1313', '5a86', '36d', '42ae', 'ed9b', '1c0c', 'c2af', 'eab', 'f527', '2af1', 'bda0', '6c4b', '757a', '68e5', 'd374', 'fd54', '5647', '191e', 'bff7', '500', '251b', '4f16', 'd4b0', 'f3c3', 'bdaa', 'f883', '1b4f', '91d0', 'bf81', '2da4', 'b645', '59e9', '6e42', '6856', '6c6f', '10bc', '7f89', 'e056', 'd4db', '2afe', 'daff', '8989', 'eec9', 'b4e3', 'a882', '8d6e', '198a', '8d96', '4482', 'f9a7', '8e47', 'b447', '8ceb', 'c55b', '6dbc', '5e05', '428f', '9d4a', '20b3', '9898', 'b2e9', '7cb8', '53c2', '878c', '7b2b', 'b241', '9b59', 'c591', '952e', 'b4e9', '2ef', '6f5e', '641c', '9b9e', '38e1', '1d51', 'b5a2', '22fa', 'c5ea', '5465', '8bc6', 'f5c1', 'd950', '3b09', '1efb', '5c5f', '1ade', '81ef', '7dbd', '8214', '708a', '7a07', 'de5f', '75f3', '75a2', 'cec7', '7fdf', '802c', '2484', 'd6a2', '743a', 'badf', '3443', 'd205', 'cc0d', 'e622', '815b', 'd6cf', '2581', '6ad7', '7583', '6a93', 'a309', 'ff3', 'eb8c', '1498', 'c1ba', 'ba1e', '935', '4bdb', '77b9', '66c0', 'eaba', 'f8e3', '77c4', 'cb26', '4da0', '7c4c', '53dd', 'f16a', '2a88', 'e74e', '813a', '629a', '6464', '8e94', '252f', '2cf', '8e4a', 'b45c', '22b3', 'fd73', '696e', '5ac5', '62cc', '7ac2', '74f2', '56a6', '6396', '1712', '21ac', '4bc7', 'bf4', '597f', '3a17', 'a4e5', '3b5a', 'e674', '766', '16ee', '554c', '6aea', 'f3aa', '7b45', '34d1', '2aad', 'a905', '2b49', 'd944', 'a6ed', '3a1a', '5229', '4ad4', '55f4', '2c9', '6308', '725f', '4e7c', '9d7a', 'aecf', 'de8', 'f906', '1091', '3fa2', 'abf6', 'ca08', 'a3a0', 'c30a', '7d40', '4067', '1f1', '351', '420f', 'b59d', '808e', '264d', 'd520', '3bd3', '6e96', 'd426', 'afe4', '3643', 'd91f', 'f229', '2d1c', '3b2d', 'a811', '8e51', 'f9da', 'd5b2', '92a6', '1797', 'f364', 'c440', '2af7', 'db5', '6abf', '889', 'ce10', 'c816', '5642', 'bf3f', '293f', '393e', '3bb5', '5fb0', '24a5', 'af0', '2b6e', 'b05a', 'afed', '304a', '1878', '2285', '4fe6', 'ffb', '4cf9', '8d1f', '1ec3', 'aa2a', '154c', '57c8', '6ddc', '1083', '3f05', '45d3', 'cf30', 'd8e0', '123d', '56e', 'd0da', '1374', 'a86', 'aee4', 'c5f8', '7909', '8e4', '122b', '9a5e', 'c929', '196', 'c50c', '54d2', '10b5', 'd40', '3f89', 'a6df', '2558', '3f24', '275', 'efbe', 'a9e8', '9f28', '250f', 'fc43', '462', '161', '75d6', '314a', '8c4e', '6be4', 'faae', 'f642', '419', '36dc']

b = ['d179', '4f2', '40c7', '23e8', 'db62', '58e', 'c446', 'f505', '1a99', 'afd', '2671', 'e9ef', 'a719', '67d', '8510', '8302', '33b0', '95e3', 'e17a', 'b730', 'faf', '325b', '6169', 'bad', '58e3', 'a0a7', '4a88', '1218', '3095', '9363', '8973', '1ac4', '755e', 'ae83', 'f040', '5e86', 'a210', '3a1f', '1b8a', '542e', 'aa10', '7598', '4ae1', 'cd28', '2479', '3a33', '4716', '5a63', '6bf2', '2b1d', '2a51', '349e', '2ab9', '2a92', '6a75', 'c084', '2b66', '2b37', '51f1', '25b4', '41c2', 'b386', '6159', 'f9af', '2ee3', '5de7', '129e', '6c2b', 'c7b5', '37cc', 'f82', 'de82', '8a59', '43e8', 'c1a', '6f63', '80d', '83d5', 'a545', 'a731', 'e229', '1719', '3800', '48c2', 'fce1', '6fe0', '9102', '7338', 'c017', '23c1', '4cb0', '103f', '7a46', 'c56a', '49a8', 'fb62', '512a', 'eef2', '8017', '347b', 'ba69', '5db3', '13c5', '5a84', 'ef72', '631f', '49fe', 'ab46', '6c63', '6466', '51fb', 'f352', '941d', '26c5', '4f51', '71af', '1b0d', '9f66', '3c4', '75e1', 'e0b9', '3e02', 'a417', 'a5cf', 'e2c5', '40b', 'aff5', '7c8c', 'd6ca', '6517', '884a', '383c', '7e95', '5f7e', '149e', 'ea8e', '9227', '1479', 'f5dc', '7eef', '6cf5', 'e916', '8003', 'ee0c', '32cf', '8f75', '9d3c', '128b', '89c8', '993d', '59b7', '9083', '1e0f', 'e367', '33c', '1fd2', 'f562', '92fc', 'f2e4', '17f', '8055', '64de', 'fdde', '9721', 'bd2b', '433c', '349d', '93b3', 'b2da', '6d1e', 'd39f', '944', '5600', '5bfb', '1e4d', 'a30f', '8594', '518f', 'c647', '3194', 'd2cc', '7748', 'ba0a', 'a3ab', '2e1', 'f244', '5b96', 'e446', 'd0cb', '9ee', '48fc', '1a04', 'aaac', '5d29', '4c12', 'e5ac', 'f628', 'f6e5', '3d29', 'e0c4', '4449', '652f', 'b84f', 'c616', 'fb81', '8525', '6249', 'abe8', 'da36', '9b4d', 'baba', '78b5', 'da78', 'ab28', '5848', 'b8ff', 'afc9', '7747', 'bc49', '7735', 'b9c3', '364f', 'c285', 'fbef', '5ab0', 'a2b2', 'c232', 'a39e', 'fefc', 'd306', 'c604', 'e24f', '809', 'de44', '312', 'c6f5', '2969', 'e41c', 'd4ee', '1fae', '4fd9', 'f7f0', '913', 'aa23', '34d8', '3faa', 'cc17', 'b217', 'af89', 'd548', '6140', 'd46c', 'cce', 'ea89', '51fd', '1139', 'd6b6', '20dd', '302d', 'c729', 'fa5c', 'd77a', 'd90a', 'ed83', 'd71a', 'e067', 'be15', 'ef7c', '39e9', '2c0f', 'e219', '5972', '419f', '98d', 'ef15', 'fb39', 'd3b0', 'b3f3', 'e7ed', '3b9f', '6761', 'e888', 'f65b', '280', 'dd9e', 'e9ef', 'c806', '7cc8', 'f515', '418d', 'f11f', '8f3b', 'e43c', '6721', '789f', 'f92c', '73f9', 'f290', '6064', 'cf2d', '673a', '5177', 'fdb1', '1109', '5cf3', '3757', 'f387', '11f4', '533a', 'a15e', '71f6', 'ff08', 
'4b63', 'fc42', '51e8', 'c9a0', 'ff7f', 'e6d9', '6c5b', 'ff68', '44d4', 'aa83', 'f36f', 'ff2c', '9c4d', '3e64', '61e1', 'd644', 'ff27', '796', '2263', '65a8', 'fd15', '8e42', '70aa', '19ca', 'f075', 'f69c', 'ddee', '34f8', '3b2', 'bad7', '243a', '7c4a', 'd752', 'f213', 'a1bb', '322', '95f0', '8796', 'd4a5', 'f20b', '908f', 'eb28', '9a27', '8bb2', 'ed6c', 'c9df', '9965', 'd691', '8b4f', '6ce4', 'ec99', 'de21', 'e297', 'dcad', 'c85d', 'e3ee', '5eb0', '6b54', 'd0af', '3b8', 'd7ce', '6211', 'e989', 'e19a', '2d5c', '28d7', '718b', 'dc8c', '174a', 'f83f', 'c0e3', '909', 'a42f', '75c3', 'd781', 'b9fb', '8979', '9408', 'ae07', '1920', 'd14d', 'a7c4', 'bf4b', '7a67', '56ea', 
'77bd', 'b32f', 'a39', 'cf1a', '6547', 'f12c', '4eeb', 'ded9', 'fbab', 'cbf6', '3f55', '72bd', '8fe5', '20b9', '273c', 'c471', '86f0', '1313', 'c105', 'bf22', 'bb65', 'ebd5', '871c', '30d0', 'c2af', '34e2', 'ae8e', '8e0b', 'bda0', '5dda', 'bff7', '4f16', 'c476', 'bdaa', '3f54', '8ba1', '1b4f', 'c70d', '2f50', 'b645', '59a2', '10bc', 'c011', 'b4e3', '4541', '764', '8d96', '120b', '5200', 'b447', 'a7b', '5e05', '405b', 'eaf5', 'b2e9', 'face', '878c', 'd288', 'b241', '6f5e', 'e58c', 'c8a3', '9b9e', '5f21', 'afcc', '1d51', '440c', '2669', '6a01', '2d08', '8bc6', '3c2e', 'a152', '35eb', '8c2c', '1efb', '81ef', '2c57', '7ef8', '75f3', 'c91a', '10eb', 'ff81', '7fdf', '69f3', 'df43', 'ef99', '2484', '23e7', '743a', 'fdda', 'af7e', '2581', '874c', '12d', 'fbf4', 'c900', '6a93', '34da', 'c47e', '2efb', 'ec8c', '1498', '50c0', '3670', '4036', 'afe5', '66c0', '6cb5', '53dd', 'c1e', '49d1', 'f421', '6464', 'b86e', '22b3', 'cfc6', '5ac5', '2b2e', '8b2e', '56a6', '1a22', '3f24', '6f58', '597f', '3b5a', '554c', '8d5', '786b', '2b49', '5229', 'b6bf', 'c0b2', '2c9', '4ffa', '4e7c', '764b', 'd9c4', '1091', '8c12', '4067', 'c28d', '61a1', 'f63b', 'fd7a', '351', 'b22e', 'afe4', 'b33d', '688c', '5d18', '3bd3', '1d71', '29a', '3b57', '3643', 'fc4a', '3b2d', '5b05', 'e8ef', '1797', '5de', 'e6b9', '8206', '6892', '2af7', '6ac1', '1ebc', '2689', 'db5', '5afe', '293f', '50eb', '574b', 'af0', '57b8', '48c9', '4986', '1878', '84e3', '6862', 'ffb', '9570', '154c', '6f03', 'e24a', 'e059', 'd4f', '534f', '79ad', '1083', 'c545', '2f6f', '123d', '6ffa', '2d05', '9c63', 'fd97', 'a86', '122b', '9a77', '73d7', '196', '344e', '1861', '10b5', 'da67', 'ddec', '6ff8', '8352', '44a9', 'fa3f', '275', '11c3', '2e97', '462', '2a9d', '13db', 'cd41', '161', 'e27', '1a17', '419', 'c12b', '6d08', 'ca90', 'b8c6']
print('a',len(a),'b',len(b))
print('lcs',lcs(a,b))


def lbs(arr): 
    n = len(arr) 
  
  
    # allocate memory for LIS[] and initialize LIS values as 1 
    # for all indexes 
    lis = [1 for i in range(n+1)] 
  
    # Compute LIS values from left to right 
    for i in range(1 , n): 
        for j in range(0 , i): 
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 
                lis[i] = lis[j] + 1
  
    # allocate memory for LDS and initialize LDS values for 
    # all indexes 
    lds = [1 for i in range(n+1)] 
      
    # Compute LDS values from right to left 
    for i in reversed(range(n-1)): #loop from n-2 downto 0 
        for j in reversed(range(i-1 ,n)): #loop from n-1 downto i-1 
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 
                lds[i] = lds[j] + 1 
  
  
    # Return the maximum value of (lis[i] + lds[i] - 1) 
    maximum = lis[0] + lds[0] - 1
    for i in range(1 , n): 
        maximum = max((lis[i] + lds[i]-1), maximum) 
      
    return maximum 
dummy = ['04f2', '40c7', '058e', '1a99', '067d', 'e17a', '0bad', '4a88', '1218', '9363', '1ac4', 'a210', '1b8a', '542e', '2479', '5a63', '2a51', '6a75', '2b37', '41c2', '2ee3', '6c2b', '37cc', 'de82', '43e8', '83d5', '48c2', '7338', 
'4cb0', '7a46', '512a', 'ba69', '631f', 'ab46', '6466', '941d', '71af', '9f66', '75e1', 'a5cf', '7c8c', 'd6ca', '7e95', 'ea8e', '7eef', 'e916', '8003', '8f75', '89c8', '993d', '9083', 'e367', '92fc', '9721', '93b3', 'd39f', 'a30f', 'c647', 'a3ab', 'e446', 'aaac', 'f6e5', 'b84f', 'baba', 'b8ff', 'bc49', 'b9c3', 'c285', 'c232', 'fefc', 'c604', 'de44', 'c6f5', 'f7f0', 'cc17', 'd548', 'd46c', 'ea89', 'd6b6', 'fa5c', 'd77a', 'ed83', 'e067', 'ef7c', 'e219', 'fb39', 'e7ed', 'f65b', 'e9ef', 'f515', 'f11f', 'f92c', 'f290', 'fdb1', 'f387', 'ff08', 'fc42', 'ff7f', 'ff68', 'aa83', 'ff2c', '61e1', 'ff27', '2263', 'fd15', '70aa', 'f69c', '34f8', 'f213', '95f0', 'f20b', 'eb28', 'ed6c', '9965', 'ec99', 'de21', 'e3ee', 'd0af', 'e19a', '28d7', 'dc8c', 'a42f', 'd781', 'b9fb', 'd14d', 'bf4b', 'cf1a', '4eeb', 'cbf6', '8fe5', 'c471', '1313', 'c2af', 'bda0', 'bff7', '4f16', 'bdaa', '1b4f', 'b645', '10bc', 'b4e3', '8d96', 'b447', '5e05', 'b2e9', '878c', 'b241', '6f5e', '9b9e', '1d51', '8bc6', '1efb', '81ef', '75f3', '7fdf', '2484', '743a', '2581', '6a93', '1498', '66c0', '53dd', '6464', '22b3', '5ac5', '56a6', '597f', '3b5a', '554c', '2b49', '5229', '02c9', '4e7c', '1091', '4067', '0351', 'afe4', '3643', '3b2d', '1797', '2af7', '0db5', '293f', '0af0', '1878', '0ffb', '154c', '1083', '123d', '0a86', '122b', '0196', '10b5', '0275', '0462', '0161', '0419']

print(lbs(dummy))

print(dummy[-3:])