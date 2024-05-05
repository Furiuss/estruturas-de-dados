def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    
fatorial_de_5 = factorial(5)
print(fatorial_de_5)