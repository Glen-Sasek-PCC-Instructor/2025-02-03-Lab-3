import math

n = int(input("POSITIVE INT PLEASE: "))
print("THANK YOU")

width = int(math.log(10 * n, 10)) + 1

for i in range(1, 11):
    print('{:>5}'.format(i), "*", n, "=", '{:>{w}}'.format(i * n, w = width))