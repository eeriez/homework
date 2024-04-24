def test(n, *args, sum=10):
    print(n, *args, sum)
    print()

test(2, 4, 5, 6, 7, 8, 9, sum=67890)

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = n * factorial(n-1)
        return fact

print(factorial(10))
