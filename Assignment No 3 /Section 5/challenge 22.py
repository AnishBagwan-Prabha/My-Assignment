class Employee:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

e1 = Employee(101, "Rohan", "HR")
e2 = Employee(102, "Kavita", "IT")

print(e1.id, e1.name, e1.department)
print(e2.id, e2.name, e2.department)