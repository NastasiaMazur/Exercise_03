#1

def count_vowels(text):
    if not isinstance(text, str):
        return 42

    vowels = 'aeiou' # or vowels = 'aeiouAEIOU' (what is better?)
    count = 0

    for i in text.lower():
        if i in vowels:
            count += 1

    return count


text = "It's a wonderful day!"
print(count_vowels(text))


#2

def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0

    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance += 1

    return distance


text1 = 'cat dog'
text2 = 'kat cat'

distance = hamming(text1, text2)
print(distance)


#3

class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"


car = Car("Red", "Gasoline", 5)
print(car)

bus = Bus("Blue", "Diesel", 50)
print(bus)


#4

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"


book1 = Book('Dune', 'Frank Herbert')
print(book1)


#5

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class BookShelf:
    def __init__(self):
        self.books = []

    def add_book_list(self, books):
        for book in books:
            if isinstance(book, Book):
                self.books.append(book)

    def books_by_author(self, author):
        return [book.title for book in self.books if book.author == author]

    def get_books(self):
        return [book.title for book in self.books]

    def clear_shelf(self):
        self.books = []


shelf = BookShelf()

book1 = Book("Animal Farm", "George Orwell")
book2 = Book("Harry Potter", "Joanne Rowling")
book3 = Book("1984", "George Orwell")
shelf.add_book_list([book1, book2, book3])

print(shelf.get_books())

print(shelf.books_by_author("George Orwell"))

shelf.clear_shelf()
print(shelf.get_books())
