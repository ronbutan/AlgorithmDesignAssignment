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
print(twoSum([2,7,11,15],9))

def isPalindrome(self, x):
    s = str(x)
    if len(s) == 2:
        return s[0] == s[1]
    mid = len(s) // 2
    s1 = s[0:mid]
    s2 = s[mid+1]
    return s1 == s2[::-1]

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
    j = 0
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

n = 785670
count = 0
while n > 0:
    n = n // 10
    count += 1
print(count)

num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revered Number ", reverse_number)