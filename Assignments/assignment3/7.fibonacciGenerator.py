# 7. Using a while loop, generate Fibonacci numbers until the next number would exceed 200. Store them in a list and print the list.

fibonacciNums = []
a, b = 0, 1

if a < 200:
    fibonacciNums.append(a)
if b < 200:
    fibonacciNums.append(b)

while True:
    nextFib = a + b
    if nextFib > 200:
        break
    fibonacciNums.append(nextFib)
    a, b = b, nextFib

print(f"Fibonacci numbers up to 200: {fibonacciNums}")