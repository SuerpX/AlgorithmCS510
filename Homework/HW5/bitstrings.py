
def num_no(n):
    nn = {0: 1, 1: 2}
    if n not in nn:
        nn[n] = num_no(n - 1) + num_no(n - 2)
    return nn[n]

def num_yes(n):
    ny = {0: 0, 1: 0}
    if n not in ny:
        ny[n] = num_yes(n - 1) + 2 ** (n - 2) # + num_yes(n - 2)
    return ny[n]

def fib(n, cache={0:1, 1:1}):
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

def fib2(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b
    return b
print(num_no(3))
print(num_yes(3))

print(fib(100))
print(fib2(1))
