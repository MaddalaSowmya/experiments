def factorial_func(n):
    if n<=1:
        return 1
    else:
        return n*factorial_func(n-1)

print(factorial_func(5))