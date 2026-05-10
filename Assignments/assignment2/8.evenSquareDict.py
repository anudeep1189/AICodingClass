# 8.  Given a list of numbers from 1 to 10, use dictionary comprehension to create a dictionary where only even numbers are keys and their squares are values. Print the resulting dictionary.

listNum = [1,2,3,4,5,6,7,8,9,10]

even_squares = {x: pow(x,2) for x in listNum if x % 2 == 0}

print(even_squares)