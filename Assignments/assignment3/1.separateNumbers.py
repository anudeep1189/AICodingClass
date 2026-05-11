# 1. Write a program that takes a list of integers and separates them into three lists: positive, negative, and zero. Then print all three lists.

numbers = [1, -2, 0, 5, -10, 0, 7, -3, 100, -50]

positiveNumbers = []
negativeNumbers = []
zeroNumbers = []

for i in numbers:
    if i > 0:
        positiveNumbers.append(i)
    elif i < 0:
        negativeNumbers.append(i)
    else:
        zeroNumbers.append(i)

print(f"Positive numbers: {positiveNumbers}")
print(f"Negative numbers: {negativeNumbers}")
print(f"Zero numbers: {zeroNumbers}")