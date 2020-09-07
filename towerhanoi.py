import time
from DynArray import DynArray

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

print([i for i in range(1,65,3)])
print([i for i in range(2,65,3)])
print([i for i in range(3,65,3)])
h,g = 10,15
print(h)
print(g)
da = DynArray()
da.print()
for i in range(16):
    da.append(i + 1)
da.print()