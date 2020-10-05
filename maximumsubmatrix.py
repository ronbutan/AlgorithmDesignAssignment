# Kadane's algorithm
def maxSubArraySum(numbers):
    size = len(numbers)
    currentMax = 0
    ultimateMax = float("-inf")
    start = end = temp = 0

    for i in range(size):
        currentMax += numbers[i]
        if currentMax < 0:
            currentMax = 0
            temp = i + 1
        elif currentMax > ultimateMax:
            ultimateMax = currentMax
            start = temp
            end = i
    return start,end,ultimateMax

def maximumSubMatrix(matrix):
    left = right  = 0
    maxLeft = maxRight = maxUp = maxDown = 0
    ultimateSum = currentSum = float('-inf')
    rows = len(matrix)
    cols = len(matrix[0])
    storageMatrix = []
    
    for left in range(cols):
        storageMatrix = [0] * cols
        for right in range(left,cols):
            for r in range(rows):
                storageMatrix[r] += matrix[r][right]
            print(storageMatrix, 'at Column: ', right)
            up,down,currentSum = maxSubArraySum(storageMatrix)
            if currentSum > ultimateSum:
                ultimateSum = currentSum
                maxLeft = left
                maxRight = right
                maxUp = up
                maxDown = down
    print(maxLeft, maxRight,maxUp, maxDown, 'sum', ultimateSum)

# matrix = [
#     [1, 2, -1, 4],
#     [-8, -3, 4, 2],
#     [3, 8, 10, -8],
#     [-4, -1, 1, 7]
# ]

matrix = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]

# matrix = [
#     [2, 1, -3, -4, 5],
#     [0, 6, 3, 4, 1],
#     [2, -2, -1, 4, -5],
#     [-3, 3, 1, 0 , 3]
# ]


# n = [5,1,-5,3]
# up,down,maxSum = maxSubArraySum(n)
# print("up: {0} -- down: {1} -- max: {2}".format(up, down, maxSum))
maximumSubMatrix(matrix)
