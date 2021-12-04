# Define aclass Employee having members id, name, department, salary.
# Create a subclass called manager with member bonus.
# Define methods accept and display in both the classes.
# Create n objects of the manager class and display the details of the manager having the maximum total salary (salary+bonus).

class employee:
    elist = list()
    def __init__(self,id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.bonus = 0
        self.bonusPercent = 15

        employee.elist.append(self)

    def calcBonus(self):
        self.bonus = (float(self.salary) * (self.bonusPercent/100))
        print("bonus is " , self.bonus)

    def displayBonus(self):
        if self.bonus == 0:
            print("no bonus is given to the employee")
        else:
            print("the bonus of the employee is : " , self.bonus)
            tsal = (float(self.salary) + float(self.bonus))
            print("and the total salary is : ", tsal)
    
    def display(self):
        print("\n\nThe employee id is : " , self.id)
        print("The employee name is : " , self.name)
        print("The employee department is : " , self.department)
        print("The employee salary is : " , self.salary)
        print("The employee bonus is : " , int(self.bonus))

class manager(employee):
    def __init__(self, id, name, department, salary):
        super().__init__(id, name, department, salary)
        self.bonusPercent = 25

# creating the list for storing manager object
lst = list()

while True:
    inp = input("Enter another manager (y/n)")
    if inp.upper() == "Y":
        mid = input("Enter the manager ID : ")
        mname = input("Enter the manager Name : ")
        mdepartment = input("Enter the manager Department : ")
        mslary = input("Enter the manager salary : ")
        # creating the manager instance 
        man = manager(id = mid , name = mname , department = mdepartment , salary = mslary)
        lst.append(man)
    else:
        break

# creating variable for comparision of manager salary 
highestBonus = 0
listIndex = None

for i in employee.elist:
    i.calcBonus()
    if i.bonus > highestBonus:
        listIndex = i

listIndex.display()

