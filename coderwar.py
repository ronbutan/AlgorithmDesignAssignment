def solution(args):
    if not args:
        return ""
    
    nLen = len(args)
    output = []
    stack = []
    for i in range(nLen):
        if not stack:
            stack.append(args[i])
        elif args[i-1] + 1 == args[i]:
            if (stack[-1] != args[i]):
                stack.append(args[i])
        elif args[i-1] == args[i]:
            continue
        else:
            if len(stack) < 3:
                for num in stack:
                    output.append(f"{num}")
            else:
                output.append(f"{stack[0]}-{stack[-1]}")
            stack = []
            stack.append(args[i])
    if stack:
        if len(stack) < 3:
            for num in stack:
                output.append(f"{num}")
        else:
            output.append(f"{stack[0]}-{stack[-1]}")
    return ",".join(output)

print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 20]))
print(solution([-66,-64,-61,-59,-58,-55,-52,-49,-47,-44,-41,-40,-37,-34,-32,-31,-29,-27,-24,-24,-21,-20]))

def sum_of_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: (x[0],-x[1]))
    intervals = [list(tup) for tup in intervals]
    stack = []
    total = 0
    isIndependent = True
    for pair in intervals:
        start, end = pair
        isIndependent = True
        for i in range(len(stack)):
            aStart, aEnd = stack[i]
            if end < aStart or start > aEnd:
                continue
            elif start >= aStart and end <= aEnd:
                isIndependent = False
                break
            elif start >= aStart and end > aEnd:
                stack[i][1] = end
                isIndependent = False
                break
            elif end <= aEnd and start < aStart:
                stack[i][0] = start
                isIndependent = False
                break
        if isIndependent:
            stack.append(pair)
    for pair in stack:
        start,end = pair
        l = end - start
        total += l
    return total
print(sum_of_intervals([[1,5],[8,11]]))
