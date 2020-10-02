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