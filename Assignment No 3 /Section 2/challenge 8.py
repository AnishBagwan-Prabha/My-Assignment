class Book:
    title = ""
    author = ""
    price = 0

b1 = Book()
b1.title = "Java"
b1.author = "ABC"
b1.price = 400

b2 = Book()
b2.title = "Python"
b2.author = "XYZ"
b2.price = 600

b3 = Book()
b3.title = "SQL"
b3.author = "PQR"
b3.price = 700

print(b1.title, b1.author, b1.price)
print(b2.title, b2.author, b2.price)
print(b3.title, b3.author, b3.price)