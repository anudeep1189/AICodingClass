#7.  Use a while loop to iterate from 1 to 10. For each number, check if it's even. If even, square it; if odd, skip it. Calculate and print the total sum of all squared even numbers.

listNums = [1,2,3,4,5,6,7,8,9,10]

sumSqEvenNum = 0

for i in listNums:
    if i % 2 == 0:
        sq = pow(i,2)
        sumSqEvenNum += sq

print(f"Sum of sqaure of even number = {sumSqEvenNum}")