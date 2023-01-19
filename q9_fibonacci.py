# QUESTION 9
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_sum = 0

# Compute the sum of the first 50 Fibonacci numbers
for i in range(50):
    fib_sum += fibonacci(i)

print("The sum of the first 50 Fibonacci numbers is", fib_sum)