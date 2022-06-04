from functools import lru_cache

@lru_cache(maxsize=128)
def fib (n) :
    if n == 0  or n == 1:
        return n
    return fib(n-2) + fib(n-1)

def fib_without_cache(n):
    if n == 0  or n == 1:
        return n
    return fib(n-2) + fib(n-1)

if __name__ == "__main__":

    print(fib(30))

    print(fib_without_cache(30))