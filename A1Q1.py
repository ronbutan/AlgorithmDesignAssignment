import sys

def power_modulo(m, k, n):
    if k == 0:
        return 1
    if k % 2 == 0:
        r = power_modulo(m,k//2,n)
        return (r * r) % n
    else:
        return ((m % n) * ((power_modulo(m,k-1,n) % n))) % n

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))


'''
T(n) = T(n/2) + a, when n is even
T(n) = T(n-1) + b, when n is odd
T(0) = 1 (base case)
T(1) = T(0) + b = 1 + b
T(2) = T(1) + a = 1 + b + a

when n is odd can be written as,

T(n) = T((n-1)/2) + a + b
Let (a+b) = C,
T(n)    =   T(n/2) + C
        =   T(n/4) + 2C
        =   T(n/8) + 3C
do k times,
T(n)    =   T(n/2^k) + k(C)

Assume, n/2^k = 1, then n = 2^k

k = lg n

T(n)    =  T(1) + Clgn
        =  1 + b + a + Clgn
        = O(lgn)
'''