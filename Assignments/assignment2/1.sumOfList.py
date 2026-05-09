# 1.  Write a program that takes a list of numbers and calculates the sum of all elements. Print the total sum. (Example: [10, 20, 30] → Sum: 60)


listNum = [10,12,3,4,5,6,11.5,40,50,43.5,55]

sum = 0

for i in listNum:
    sum += i

print(f"Sum of all elements - {sum}")