import time
from math import log
first_num = 26041021264406654159
second_num = 10839626896323242159
#расширенный алгоритм Евклида
def my_ext_gcd(a, b):
    x0 = 1; y0 = 0; x1 = 0; y1 = 1; i = 1
    while b != 0:
        q = a//b; r = a % b
        if r == 0:
            break
        a = b; b = r
        xtmp = x1; ytmp = y1
        x1 = x0 - q*x1; y1 = y0 - q*y1
        x0 = xtmp; y0 = ytmp
        print("step:", i, "\nx = ", x1, "\ny = ", y1, "\nr = ", r, "\n")
        i += 1
    print("x = ", x1, "\ny = ", y1, "\nGCD = ", b)
    print("xa + yb =", first_num*x1 + second_num*y1)
#Расширенный бинарный алгоритм Евклида
def my_ext_bin_gcd(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a >>= 1; b >>= 1; g += 1
    u = a; v = b; A = 1; B = 0; C = 0; D = 1; i = 1
    while u != 0:
        print("step ", i, "\nx = ", C, "\ny = ", D, "\nr = ", g*v, "\n")
        i += 1
        while u % 2 == 0:
            u >>= 1
            if A % 2 == 0 and B % 2 == 0:
                A >>= 1; B >>= 1
            else:
                A = (A + b) >> 1; B = (B - a) >> 1
        while v % 2 == 0:
            v >>= 1
            if C % 2 == 0 and D%2 == 0:
                C >>= 1; D >>= 1
            else:
                C = (C + b) >> 1; D = (D - a) >> 1
        if u >= v:
            u = u - v; A = A - C; B = B - D
        else:
            v = v - u; C = C - A; D = D - B
    print("x = ", C, "\ny = ", D, "\nGCD = ", g*v)
    print("xa + yb =", first_num*C + second_num*D)
#Расширенный алгоритм Евклида с «усечёнными» остатками
def my_ext_trunc_gcd(a, b):
    x0 = 1; y0 = 0; x1 = 0; y1 = 1; i = 1
    while b != 0:
        q = a//b
        b, a, r = a % b, b, b
        x1, x0 = x0 - x1*q, x1
        y1, y0 = y0 - y1*q, y1
        if b > r//2:
            b = r - b
            x1 = x0 - x1
            y1 = y0 - y1
        print("step ", i, "\nx = ", x0, "\ny = ", y0, "\nr = ", r, "\n")
        i += 1
    print("x = ", x0, "\ny = ", y0, "\nGCD = ", a)
    print("xa + yb =", first_num*x0 + second_num*y0)
#timer = time.time()
#my_ext_trunc_gcd(first_num, second_num)
#my_ext_bin_gcd(first_num, second_num)
my_ext_gcd(first_num, second_num)
#print("time:", (time.time() - timer)*1000, "msec.\n")
#a = 26041021264406654159
#b = 10839626896323242159
#x1 = 232665795
#y1 = -558954194
#x2 = 7040423925105629268
#y2 = -16913850531728281667
#GCD = 8743126559
#if (y2*GCD - y1*GCD)/a == (x1*GCD - x2*GCD)/b:
#    print("ok")
#time.sleep(100000)
