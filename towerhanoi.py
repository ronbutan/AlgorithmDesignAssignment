import time



start_time = time.time()

l = [1]
print(l[-1])
end = 1
for i in range(1,len(l)):
    if (l[i-1] + 1 != l[i]):
        end = i
        break
print('out of loop')
print(l[0:end])
print("--- %s seconds ---" % (time.time() - start_time))

print(2**31 - 1)