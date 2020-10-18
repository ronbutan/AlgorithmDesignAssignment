import random
print(int('5904',16))
print(int('c19d',16))
print(int('9fee',16))
print(int('3cd5',16))
print(int('4865',16))
print(int('0545',16))
print(int('260d',16))
print(int('67',16))

random.seed(784)
l = [format(random.randint(1000,2200),'02X') for i in range(1000)]
print(" ".join(l))