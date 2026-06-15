class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("PQR School")
print(Student.school)