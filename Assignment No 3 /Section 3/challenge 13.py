class Movie:
    def __init__(self, name, hero, rating):
        self.name = name
        self.hero = hero
        self.rating = rating

m1 = Movie("KGF 2", "Yash", 8)

print(m1.name)
print(m1.hero)
print(m1.rating)