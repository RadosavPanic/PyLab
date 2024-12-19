class Employee:
    totalEmployees = 0

    def __init__(self, empName, age, designation, salary):
        self.empName = empName
        self.age = age
        self.designation = designation
        self.salary = salary
        Employee.totalEmployees = Employee.totalEmployees + 1

    def getEmpDetails(self):
        return self.empName, self.age, self.designation, self.salary

    def updateSalary(self, newSalary):
        self.salary = newSalary
        print(f"{self.empName}'s salary Updated")
        return self.salary


empOne = Employee("John", 35, "Manager", 2900)
empTwo = Employee("Sam", 26, "Python Developer", 2400)
empThree = Employee("Peter", 31, "UI/UX Designer", 2100)

empOne.updateSalary(3100)  # John's salary Updated
print(empOne.getEmpDetails())  # ('John', 35, 'Manager', 3100)
print(Employee.totalEmployees)  # 3


class Intern(Employee):
    def __init__(self, empName, age, designation, salary, internPeriod):
        # super().__init__(self, empName, age, designation, salary)  # same purpose as below
        Employee.__init__(self, empName, age, designation, salary)
        self.internPeriod = internPeriod
        self.isCompleted = False
        self.tasks = []

    def getPeriod(self):
        return f"Internship period (in months) is: {self.internPeriod}"

    def updateSalary(self, newSalary):
        print("Intern salary cannot be updated directly. Intern should change to change status to Employee first.")
        return self.salary

    def assignTask(self, taskName):
        self.tasks.append(taskName)
        print(f"Task '{taskName}' assigned to intern {self.empName}")

    def getTasks(self):
        print(f"Tasks assigned to {self.empName}: {', '.join(self.tasks)}.")
        return tuple(self.tasks)

    def deleteTask(self, taskName):
        if taskName in self.tasks:
            self.tasks.remove(taskName)
            print(f"Task '{taskName}' removed from the tasks.")
        else:
            print(f"Specified task '{taskName}' does not exist.")

    def completeInternship(self):
        self.isCompleted = True
        print(f"{self.empName}'s internship has been completed.")


internOne = Intern("Tom", 22, "Marketing Intern", 1500, 3)
print(internOne.getEmpDetails())  # ('Tom', 22, 'Marketing Intern', 1500)
print(internOne.getPeriod())  # Internship period (in months) is: 3

internOneSalary = internOne.updateSalary(1700)  # Intern salary cannot be updated directly. Intern should change to change status to Employee first.
print(internOneSalary)  # 1500

internOne.assignTask("gather market data")  # Task 'gather market data' assigned to intern Tom
internOne.assignTask("create user documentation")  # Task 'create user documentation' assigned to intern Tom
internOneTasks = internOne.getTasks()  # Tasks assigned to Tom: gather market data, create user documentation.
print(internOneTasks)  # ('gather market data', 'create user documentation')

internOne.deleteTask("organize team files")  # Specified task 'organize team files' does not exist.
internOne.deleteTask("create user documentation")  # Task 'create user documentation' removed from the tasks.
internOne.getTasks()  # Tasks assigned to Tom: gather market data.