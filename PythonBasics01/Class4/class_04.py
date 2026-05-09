a = 1 + 2 
b = 10 / 2
c = 10 * 3
d = 10 % 2
e = 10 - 5
f = 10 // 5
g = 2 ** 3
allResults = []

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
# Arithmetic operations
valA = 1 + 2
valB = 10 / 2
valC = 10 * 3
valD = 10 % 2
valE = 10 - 5
valF = 10 // 5
valG = 2 ** 3
allResults.extend([valA, valB, valC, valD, valE, valF, valG])

# Logical NOT
currentValA = 0
conditionThree = not currentValA
allResults.append(conditionThree)

a = 0
condition3 = 4
condition3 = not a 
print(f"{condition3}")
# Logical AND
currentValX = 10
allResults.append(currentValX > 5 and currentValX < 20)

x = 10 
print(x > 5 and x < 20)
# Augmented assignment
currentValX += 10
allResults.append(currentValX)

x += 10
print(x)
# Bitwise operators
bitwiseValA = 10
bitwiseValB = 4
allResults.extend([bitwiseValA & bitwiseValB, bitwiseValA | bitwiseValB, ~bitwiseValA, bitwiseValA ^ bitwiseValB, bitwiseValA >> 2, bitwiseValA << 2])

#bitwise operator
# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR
a = 10
b = 4
# Membership operator
membershipValX = 20
membershipValY = 40
myList = [10, 20, 30, 40, 50]
allResults.append(membershipValX not in myList)
myString = "hello how are you"
allResults.append("o" in myString)
allResults.append("o" not in myString)

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
# Identity operator
listXOne = [1,2]
listYOne = listXOne
allResults.append(id(listXOne))
allResults.append(id(listYOne))
allResults.append(listXOne is listYOne)

#membership 
x = 20
y = 40
list = [10, 20, 30, 40, 50]
listXTwo = [1,2]
allResults.append(id(listXTwo))

if (x not in list):
    print("x is NOT present")
listXTwo.append(4)
allResults.append(id(listXTwo))

a = "hello how are you"
print("o" in a)    
print ("o" not in a)
listYTwo = listXTwo.append(3)
allResults.append(listXTwo)
allResults.append(listYTwo)
allResults.append(id(listXTwo))
allResults.append(id(listYTwo))
allResults.append(listXTwo is listYTwo)

#identity operator
#checks the memory location not only the value 

list_x = [1,2]
list_y = list_x 

print(f"location of list_x {id(list_x)}")
print(f"location of list_y {id(list_y)}")

print(list_x is list_y)    

#-----

list_x = [1,2]
print(f"list_x before append - {id(list_x)}")

list_x.append(4)
print(f"list_x after append - {id(list_x)}")

list_y = list_x.append(3) 

print(f"list_x - {list_x}")
print(f"list_y - {list_y}")

print(f"location of list_x {id(list_x)}")
print(f"location of list_y {id(list_y)}")

print(list_x is list_y) 
# Print all collected results using a for loop
for resultItem in allResults:
    print(resultItem)