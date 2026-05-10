# 4.  Create a list of numbers from 1 to 10. Extract and print the first 3 elements, last 3 elements, and middle 4 elements using slicing.

listNums = [1,2,3,4,5,6,7,8,9,10]

firstThree = listNums[:3] 
middleFour = listNums[3:7]
lastThree = listNums[-3:]

print(f"First 3 : {firstThree}")
print(f"Middle 4:  {middleFour}")
print(f"Last 3. :     {lastThree}")


