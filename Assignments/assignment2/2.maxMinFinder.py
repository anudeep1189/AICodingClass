# 2.  Given a list of numbers, find and display both the maximum and minimum values without using built-in max() and min() functions (or with them). (Example: [45, 23, 89, 12, 56] → Max: 89, Min: 12)


listNum = [10,12,3,4,5,6,11.5,40,50,43.5,55]

max = listNum[0] 
min = listNum[0]

for i in listNum:
    if i > max:
        max = i
    
    if i < min:
        min = i

print(f"max:{max}")
print(f"min:{min}")


