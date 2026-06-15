class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

s1 = Student("Rohan", 1, 85)
s2 = Student("Anish", 2, 81)
s3 = Student("Anil", 3, 80)

print(s1.name, s1.roll_no, s1.marks)
print(s2.name, s2.roll_no, s2.marks)
print(s3.name, s3.roll_no, s3.marks)