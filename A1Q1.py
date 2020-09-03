import sys
import time

def power_modulo(m, k, n):
    if k == 0:
        return 1
    if k % 2 == 0:
        r = power_modulo(m,k//2,n)
        return (r * r) % n
    else:
        return ((m % n) * ((power_modulo(m,k-1,n) % n))) % n

""" def power_modulo(m, k, n):
    if k == 0:
        return 1
    else:
        return ((m % n) * (power_modulo(m,k-1,n) % n)) % n """

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    start_time = time.time()
    print(power_modulo(m, k, n))
    print('---- %.6g seconds ----' % (time.time() - start_time))
