#Implement iterative & recursive function for Factorial.
# FACTORIAL iterative
def calcFactorialIterative(num):
    fac = 1
    for i in range(1, num + 1):
        fac = fac * i
    return fac
num = int(input("What number would you like to find the factorial of: "))
result = calcFactorialIterative(num)
print("factorial of ", num, " is ", result)

# FACTORIAL recursive
def calcFactorialRecursive(n):
    if ( n == 0 ):
        return 1
    else:
        return n * calcFactorialRecursive(n-1)
n = int(input("Enter a number to find the factorial of using the recursion: "))
calculate = calcFactorialRecursive(n)
print("Using recursion, the factorial of ", n, " is ", calculate)
#print(calcFactorialRecursive(5))

#Fibonacci iterative
def fibonacci(n):
    terms = [0,1]
    i = 2
    while i <= n:
        terms.append(terms[i-1]+terms[i-2])
        i = i + 1
    return terms[n]
n = int(input("Enter a number you want to find the fibonacci of: "))
fibonacciIterativeResult = fibonacci(n)
print("Fibonacci of ", n, "is ", fibonacciIterativeResult)

# Fibonacci recursive
def fibRecursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2) #Two recursive calls
    return fibVal
n = int(input("Enter a number to find the fibonacci using the recursive approach: "))
fibonacciRecursive = fibRecursive(n)
print("Fibonacci of ", n, "is ", fibonacciRecursive)