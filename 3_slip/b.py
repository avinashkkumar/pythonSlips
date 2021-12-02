# B)Write a python script to define a class student having members roll no, name, age, gender. 
# Create a subclass called Test with member marks of 3 subjects.
# Create three objects of the Test class and display all the details of the student with total marks.

class student:
    def __init__(self,rollno,name,age,gender):
        self.rollno = rollno
        self.name = name
        self.age = age 
        self.gender = gender
    
class test(student):
    def __init__(self, rollno, name, age, gender, marks1, marks2, marks3):
       super().__init__(rollno, name, age, gender)
       self.marks1 = int(marks1)
       self.marks2 = int(marks2)
       self.marks3 = int(marks3)
    
    def printDetails(self):
       print("\n\nname is " + self.name)
       print("age is " , self.age)
       print("the rollno is " , self.rollno)
       print("the gender is " , self.gender)
       fmarks = (self.marks1 + self.marks2 + self.marks3)
       print("marks is " , fmarks ,"\n\n")

     

lst = []
while True:
    i = input('do you want to enter more student (y/n) : ')
    if i.upper() == "Y":
        rollno = int(input("enter students roll no "))
        name = input("enter the name ")
        age = int(input("enter the age "))
        gender = input("enter the gender ")
        marks1 = input("enter the marks of subject1")
        marks2 = input("enter the marks of subject2")
        marks3 = input("enter the marks of subject3")

        t1 = test(rollno,name,age,gender,marks1,marks2,marks3)
        lst.append(t1)
    else:
        break

for x in range(len(lst)):
    lst[x].printDetails()

