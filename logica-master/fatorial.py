def fatorial(numero):
    f = 1
    n = 1
    while n <= numero:
        f = f * n
        n = n + 1


assert fatorial(1) == 1
assert fatorial(2) == 2
assert fatorial(3) == 6
