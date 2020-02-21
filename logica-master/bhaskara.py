from math import sqrt


def baskara(a, b, c):
    delta = b ** 2 + (-4 * a * c)
    if delta > 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        print(x)
        return (x,)
    else:
        return tuple()
        else:
            x = -c / b
            return (x,)assert baskara(a=-6, b=12, c=0) == (0, 2)
            assert baskara(a=-1, b=2, c=1) == (-1,)
            assert baskara(a=-7, b=6, c=2) == ()

# x1, x2 = baskara(-6, 12, 0)
# print("""
# x1: {}
# x2: {}""".format(x1, x2))
