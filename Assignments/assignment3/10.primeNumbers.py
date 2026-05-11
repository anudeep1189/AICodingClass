# 10. Take a set of numbers and print a new sorted list containing only the prime numbers from that set. Use a helper function or conditional logic to test primality.

numbersSet = {1, 11, 2, 3, 4, 15, 56, 7, 68, 9, 10, 11, 13, 17, 21, 29, 23, 30, 37}

primeNumbers = []

for num in numbersSet:
    isPrime = True

    if num < 2:
        isPrime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break

    if isPrime:
        primeNumbers.append(num)

primeNumbers.sort()

print(f"Original list: {numbersSet}")
print(f"Sorted list of prime numbers: {primeNumbers}")
