def maxSubArraySum(numbers,size):
    currentMax = 0
    ultimateMax = float("-inf")
    start = end = temp = 0

    for i in range(size):
        if currentMax < 0 and numbers[i] > currentMax:
            currentMax = numbers[i]
            temp = i
        else:
            currentMax += numbers[i]

        # if currentMax < 0:
        #     currentMax = 0
        #     temp = i + 1
        if currentMax > ultimateMax:
            ultimateMax = currentMax
            start = temp
            end = i
    return start,end,ultimateMax
    

a = [-13, 1, -3, -25, -20, -3, -16, -23, -12, 20, 50, -15, -4, -7,-1] 
b = [10, 8, -1, -2, -19, -3, 20, 20, 6]
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))
print("Maximum contiguous sum is", maxSubArraySum(b,len(b)))