class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
      
      
emp1 = Employee("Zara", 2000)
emp2 = Employee("John", 1500)
emp3 = Employee("Jane", 2500)

print(emp1.displayCount())
emp2.displayEmployee()
