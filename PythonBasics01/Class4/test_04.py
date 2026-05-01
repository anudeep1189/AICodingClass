a = 1 + 2 
b = 10 / 2
c = 10 * 3
d = 10 % 2
e = 10 - 5
f = 10 // 5
g = 2 ** 3

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


a = 0
condition3 = 4
condition3 = not a 
print(f"{condition3}")

x = 10 
print(x > 5 and x < 20)

x += 10
print(x)

#bitwise operator
# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#membership 
x = 20
y = 40
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present")

a = "hello how are you"
print("o" in a)    
print ("o" not in a)

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