"""
Examples of memoization for self study.
"""

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib_vals = [0]*100

def memoized_fib(n):
    fib_value = 0
    if n == 0:
        fib_vals[n] = 1
        return 1
    elif n == 1:
        fib_vals[n] = 1
        return 1
    elif fib_vals[n] != 0:
        return fib_vals[n]
    else:
        fib_value = memoized_fib(n - 1) + memoized_fib(n - 2)
        fib_vals[n] = fib_value
        return fib_value

fac_vals = [0]*100
fac_vals[0] = 1

def factorial(n):
    if 0 <= n <= 1:
        return 1
    return n * factorial(n-1)

def memoized_factorial(n):
    fac_value = 1
    if n == 0 or n == 1:
        fac_vals[n] = 1
        return 1
    elif fac_vals[n] != 0:
        return fac_vals[n]
    else:
        fac_value = n * memoized_factorial(n-1)
        fac_vals[n] = fac_value
        return fac_value

memoized_factorial(10)
