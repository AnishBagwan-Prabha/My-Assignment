class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def show(self):
        print(self.name)
        print(self.subject)

t1 = Teacher("Ramesh", "Science")

t1.show()