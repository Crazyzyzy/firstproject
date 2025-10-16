class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

    def __add__(self, other):
        if self.author == other.author:
            return (self.pages + other.pages)
        else:
            return 'other authors'

King = Book('it', 'king', 400)
Steven = Book('carry', 'king', 200)
Stan = Book('Spider-man', 'stan', 500)
print(King)
print(King+Steven)
print(Steven+Stan)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f'name:{self.name}  age:{self.age}'

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025 - birth_year)

persen1 = Person('Alice', 19)
print(persen1.info)

print(Person.is_adult(20))
print(Person.is_adult(15))

persen2 = Person.from_birth_year('Bob', 2000)
print(persen2.info)