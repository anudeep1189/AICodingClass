#5.  Given a list of numbers, ask the user to enter a number and count how many times that number appears in the list. Print the count. (Example: [1, 2, 3, 2, 2, 4] → Enter 2 → Count: 3)

ListNums = [1, 2, 3, 2, 2, 4]
print(f"List numbers : {ListNums}")

UserInput = input("Enter number to count : ")

searchNum = int(UserInput)
count = ListNums.count(searchNum)

print(f"Number appears : {count}")