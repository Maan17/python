#check if an employee has achieved his weekly target or not
class Employee:
    #class attribute
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been acheved")

employeeOne = Employee()
print(employeeOne.name)
print(employeeOne.hasAchievedTarget())

#instance attribute
employeeOne.age = 45
