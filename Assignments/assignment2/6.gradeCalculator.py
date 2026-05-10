#6.  Write a program that takes a test score (0-100) as input. Use nested if-elif-else statements to assign grades: A (90-100), B (80-89), C (below 80). Handle invalid scores (below 0 or above 100).

inputMarks = float(input("Enter marks : "))

if inputMarks >= 90:
    grade = 'A'
elif inputMarks >= 80:
    grade = 'B'
else:
    grade = 'C'

print(f"Grade : {grade}")            
