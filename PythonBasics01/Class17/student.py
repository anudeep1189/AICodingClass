class Student:
    "A student enrolled in the course"

    #constructor
    def __init__(self,name,marks):
        print("Constructor called from the student class")
        self.name = name
        self.marks = marks

    def Display():
        #display
        print(self.marks)
        print(self.name)

#create the student object
s_obj = Student("John", 85)
s_obj.Display()

s_obj = Student("hyg",95)
s_obj.Display()



print(type(s_obj)) #<class '__main__.Student'>
print(type(Student)) #<class 'type'>
print(isinstance(s_obj,Student)) #true , checking if the s_obj is the obj of the student or not 

