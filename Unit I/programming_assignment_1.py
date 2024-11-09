import math


def my_sqrt(a):
    x = 1
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            return y
        x = y


def test_sqrt(n):
    a = 1
    while a <= n:
        mysqrt = my_sqrt(a)
        mathsqrt = math.sqrt(a)
        diff = abs(mysqrt - mathsqrt)
        print(
            f'a = {a} | my_sqrt(a) = {mysqrt} | math.sqrt(a) = {mathsqrt} | diff = {diff}')
        a = a + 1


test_sqrt(25)
