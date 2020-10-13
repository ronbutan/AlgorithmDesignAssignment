from typing import List

# 1351. Count Negative Numbers in a Sorted Matrix
def countNegatives(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0
    rLen = len(grid)
    cLen = len(grid[0])
    row = 0
    counter = 0
    left = 0
    right = cLen - 1
    while left <= right and row < rLen:
        if grid[row][0] < 0:
            counter += cLen
            row += 1
            continue
        elif grid[row][-1] >= 0:
            row += 1
            continue
        else:
            mid = left + ((right - left) // 2)
            if grid[row][mid] >= 0:
                left = mid + 1
            else:
                right = mid
            
            if left >= right:
                counter += (cLen - left)
                left = 0
                right = cLen - 1
                row += 1
    return counter

'''
Sample Input
[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
[[8,7,4,-1],[7,6,3,-2],[2,0,-1,-9],[0,-1,-2,-11]]
[[-1]]
[[0]]
'''

# 35. Search Insert Position

def searchInsert(self, nums: List[int], target: int) -> int:
    if not nums:
        return 0
    nLen = len(nums)
    if target > nums[-1]:
        return nLen
    if target < nums[0]:
        return 0
    
    left = 0
    right = nLen - 1
    
    while left < right:
        mid = left + ((right - left) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

'''
Sample Input
[1,3,5,6]
5
'''

# 50. Pow(x, n)
def myPow(self, x: float, n: int) -> float:
    if x <= -100 or x >= 100:
        return x
    if n == 0:
        return 1
    
    isEven = (n % 2 == 0)
    result = 0
    if n < 0 and n >= -2147483648:
        if isEven:
            result = self.myPow(x,-n//2)
            return 1 / (result * result)
        else:
            return 1 / (x * self.myPow(x,-n-1))
    else:
        if isEven:
            result = self.myPow(x,n//2)
            return (result * result)
        else:
            return (x * self.myPow(x,(n-1)))
'''
Sample Input
2.00
10
'''
# 84. Largest Rectangle in Histogram
def maximumHistogram(matrix):
    if not matrix:
        return 0
    stack = []
    nLen = len(matrix)
    index = 0
    prevIndex = 0
    area = 0
    maxArea = -1
    while index < nLen:
        if not stack or matrix[stack[-1]] <= matrix[index]:
            stack.append(index)
            index = index + 1
            continue
        else:
            prevIndex = stack.pop()
            if stack:
                area = matrix[prevIndex] * (index - stack[-1] - 1)
            else:
                area = matrix[prevIndex] * index
        maxArea = max(maxArea, area)

    while stack:
        prevIndex = stack.pop()
        if stack:
            area = matrix[prevIndex] * (index - stack[-1] - 1)
        else:
            area = matrix[prevIndex] * index
        maxArea = max(maxArea, area)
    return maxArea
'''
maximumHistogram([1,2,2,3,0,1])
'''
# 85. Maximal Rectangle
def maximalRectangle(matrix):
    if not matrix:
        return 0
    rLen = len(matrix)
    cLen = len(matrix[0])
    area = 0
    maxArea = 0
    matrix = [[int(col) for col in r] for r in matrix]
    storageMatrix = [0] * cLen

    for row in range(rLen):
        for col in range(cLen):
            if matrix[row][col] == 0:
                storageMatrix[col] = 0
            else:
                storageMatrix[col] += matrix[row][col]
        area = maximumHistogram(storageMatrix)
        maxArea = max(maxArea, area)
    return maxArea
#print(maximalRectangle([["0","0"]]))

# 125. Valid Palindrome
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''
def isPalindrome(s: str) -> bool:
    s = ''.join(c for c in s if c.isalnum())
    if s[::-1].lower() == s.lower():
        return True
    return False
print(isPalindrome("ron tan"))

# 45. Jump Game II

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
'''
def jump(nums: List[int]) -> int:
    if not nums:
        return 0
    if nums[0] == 0:
        return 0
    nLen = len(nums)
    if nLen == 1:
        return 0
    moves = [float('inf')] * nLen
    moves[0] = 0
    for i in range(0,nLen):
        n = nums[i]
        while n:
            if i + n < nLen:
                least = min(moves[i] + 1, moves[i+n])
                moves[i+n] = least
            n-=1
    return moves[-1]


# 415. Add Strings
'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
'''
def addStrings(self, num1: str, num2: str) -> str:
    carry = 0
    n1 = len(num1) - 1
    n2 = len(num2) - 1
    n3 = n1 if n1 >= n2 else n2
    res = []
    while n2 >= 0 or n1 >= 0:
        dig1 = ord(num1[n1]) - ord("0") if n1 >= 0 else 0
        dig2 = ord(num2[n2]) - ord("0") if n2 >= 0 else 0
        
        add = dig1 + dig2 + carry
        
        carry = 1 if add > 9 else 0
        res.append(str(add%10))
        n1 -=1
        n2-=1
        
    if carry == 1:
        res.append(str(carry))
    res = res[::-1]
    
    return "".join(res)