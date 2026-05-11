# 9. Write a program with a match/case statement that accepts a command like add, remove, update, or show and performs the corresponding operation on a dictionary of student names and marks.

studentsMarks = {
    "Alice": [85, 90, 92],
    "Bob": [70, 75, 68],
    "Charlie": [95, 88, 90]
}

print("Available commands: add, remove, update, show, exit")

command = input("Enter a command: ").lower()

match command:
    case 'add':
        name = input("Enter student name: ")
        marksStr = input("Enter marks (comma-separated, e.g., 80,90,75): ")
        marks = []

        for mark in marksStr.split(','):
            marks.append(int(mark))

        studentsMarks[name] = marks
        print(f"Student '{name}' added with marks {marks}.")

    case 'remove':
        name = input("Enter student name to remove: ")
        if name in studentsMarks:
            del studentsMarks[name]
            print(f"Student '{name}' removed.")
        else:
            print(f"Student '{name}' not found.")

    case 'update':
        name = input("Enter student name to update: ")
        if name in studentsMarks:
            marksStr = input(f"Enter new marks for {name} (comma-separated, current: {studentsMarks[name]}): ")
            marks = []

            for mark in marksStr.split(','):
                marks.append(int(mark))

            studentsMarks[name] = marks
            print(f"Marks for '{name}' updated to {marks}.")
        else:
            print(f"Student '{name}' not found.")

    case 'show':
        if studentsMarks:
            for name, marks in studentsMarks.items():
                print(f"{name}: {marks}")
        else:
            print("No students in the dictionary.")

    case 'exit':
        print("Exiting program.")

    case _:
        print("Invalid command. Please choose from 'add', 'remove', 'update', 'show', or 'exit'.")
