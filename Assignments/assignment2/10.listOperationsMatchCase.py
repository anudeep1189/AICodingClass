#10. Write a program that asks the user to choose an operation: 'even', 'odd', 'square', or 'cube'. Based on the choice, filter or transform a list of numbers [1-10] using list comprehension and the match/case statement. Display the appropriate results.

listNums = [1,2,3,4,5,6,7,8,9,10]

print("Option \n 1.Even \n 2.Odd \n 3.square \n 4.Cube")
userchoice = input("Choose an operation: ")

match userchoice:
    case '1':
        result = [x for x in listNums if x % 2 == 0]
        print(f"Even numbers: {result}")
        
    case '2':
        result = [x for x in listNums if x % 2 != 0]
        print(f"Odd numbers: {result}")
        
    case '3':
        result = [pow(x,2) for x in listNums]
        print(f"Squared numbers: {result}")
        
    case '4':
        result = [pow(x,3) for x in listNums]
        print(f"Cubed numbers: {result}")
        
    case _:
        print("Invalid choice! Please choose from even, odd, square, or cube.")