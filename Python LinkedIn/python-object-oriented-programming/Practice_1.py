# OOPS

# 1

# # create a basic class
# class Book:
#     def __init__(self, title):
#         self.title = title
    
# # create instances of the class
# book1 = Book("Brave New World")
# book2 = Book("War and Peace")

# # print the class and property
# print(book1) # prints the object
# print(book1.title)

# 2

# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price
#         self.__secret = "This is a secret attribute"
    
#     def  getprice(self):
#         if hasattr(self, "_discount"):
#             return self.price - (self.price * self._discount)
#         else:
#             return self.price
    
#     def setdiscount(self, amount):
#         self._discount = amount # internal to class
      
# book1 = Book("Brave New World", "Leo Tolstoy", 1225, 39.95)
# book2 = Book("War and Peace", "JD Salinger", 234, 29.95)

# # print(book1.getprice()) 
# # print(book2.getprice())
# # book2.setdiscount(0.25)
# # print(book2.getprice())
# # print(book2.__secret)
# print(book2._Book__secret)

# 3

# class Book:
#     def __init__(self, title):
#         self.title = title
        
# class Newspaper:
#     def __init__(self, name):
#         self.name = name
        
# # create some instances of the class
# b1 = Book("The Catcher In THe Rye")
# b2 = Book("The Grapes of Wrath")
# n1 = Newspaper("The Washington Post")
# n2 = Newspaper("The New York Times")

# # use type() to inspect the object type
# print(type(b1))
# print(type(n1))

# # Compare two types together
# print(type(b1) == type(b2))
# print(type(n1) == type(b1))

# # use instantance to compare a specific instance to a known type
# print(isinstance(b1, Book))
# print(isinstance(n1, Newspaper))
# print(isinstance(n2, Book))
# print(isinstance(n2, object))

# 4
# type() returns the specific class or type of an object, while isinstance() checks if an object is an instance of a particular class or its subclasses

# class Book:
#     # properties defined at class level are shared by all instances
#     BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    
#     # double-underscore propertirs are hidden from other classes
#     __booklist = None
    
#     # create class method
#     @classmethod
#     def get_book_types(cls):
#         return cls.BOOK_TYPES
    
#     # create a static method
#     def getbooklist():
#         if Book.__booklist == None:
#             Book.__booklist = []
#         return Book.__booklist
    
#     # instance method receive a specific object instance as an argument and operate on data specific to that object instance
    
#     def set_title(self, newtitle):
#         self.title = newtitle
        
#     def __init__(self, title, booktype):
#         self.title = title
#         if (not booktype in Book.BOOK_TYPES):
#             raise ValueError(f"{booktype} is not a valid book type")
#         else:
#             self.booktype = booktype
        
# # access the class attribute
# print("Book Types", Book.get_book_types())

# # Create some book instances
# b1 = Book("Title1", "HARDCOVER")
# b2 = Book("Title1", "PAPERBACK")

# # use static method to access a singleton object
# thebooks = Book.getbooklist()
# thebooks.append(b1)
# thebooks.append(b2)
# print(thebooks)

# CHALLENGE

# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"

# # ~~~~~~~~~ TEST CODE ~~~~~~~~~
# msft = Stock("MSFT", 342.0, "Microsoft Corp")
# goog = Stock("GOOG", 135.0, "Google Inc")
# meta = Stock("META", 275.0, "Meta Platforms Inc")
# amzn = Stock("AMZN", 135.0, "Amazon Inc")

# print(msft.get_description())
# print(goog.get_description())
# print(meta.get_description())
# print(amzn.get_description())

# class Stock:
#     def __init__(self, Ticker, Price, Company):
#         self.ticker = Ticker
#         self.price = float(Price)
#         self.company = Company
        
#     def get_description(self):
#         return f"{self.ticker} : {self.company} -- ${self.price}"
    
# msft = Stock("MSFT", 342.0, "Microsoft Corp")
# goog = Stock("GOOG", 135.0, "Google Inc")
# meta = Stock("META", 275.0, "Meta Platforms Inc")
# amzn = Stock("AMZN", 135.0, "Amazon Inc")

# print(msft.get_description())
# print(goog.get_description())
# print(meta.get_description())
# print(amzn.get_description())
        
# 5

# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.price = price
#         self.author = author
#         self.pages = pages

# class Magazine:
#     def __init__(self, title, publisher, price, period):
#         self.title = title
#         self.price = price
#         self.period = period
#         self.publisher = publisher

# class Newspaper:
#     def __init__(self, title, publisher, price, period):
#         self.title = title
#         self.price = price
#         self.period = period
#         self.publisher = publisher

# b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
# n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
# m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

# print(b1.author)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)

# Inheritance for above code

# class Publication:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price

# class Periodical(Publication):
#     def __init__(self, title, price, period, publisher):
#         super().__init__(title, price)
#         self.period = period
#         self.publisher = publisher
    
# class Book(Publication):
#     def __init__(self, title, author, pages, price):
#         super().__init__(title, price)
#         self.author = author
#         self.pages = pages

# class Magazine(Periodical):
#     def __init__(self, title, publisher, price, period):
#         super().__init__(title, price, period, publisher)

# class Newspaper(Periodical):
#     def __init__(self, title, publisher, price, period):
#         super().__init__(title, price, period, publisher)

# b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
# n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
# m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

# print(b1.author)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)

# 6 : Abstract based classes

# Using Abstract Base Classes to enforce class constraints
# from abc import ABC, abstractmethod

# class GraphicShape(ABC):
#     def __init__(self):
#         super().__init__()

#     @abstractmethod
#     def calcArea(self):
#         pass

# class Circle(GraphicShape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)

# class Square(GraphicShape):
#     def __init__(self, side):
#         self.side = side
    
#     def calcArea(self):
#         return self.side * self.side

# # g = GraphicShape()

# c = Circle(10)
# print(c.calcArea())
# s = Square(12)
# print(s.calcArea())

# 7 : Multiple inheritance

# class A:
#     def __init__(self):
#         super().__init__()
#         self.prop1 = "prop1"
#         self.name = "Class A"

# class B:
#     def __init__(self):
#         super().__init__()
#         self.prop2 = "prop2"
#         self.name = "Class B"

# class C(A, B):
#     def __init__(self):
#         super().__init__()
    
#     def showprops(self):
#         print(self.prop1)
#         print(self.prop2)
#         print(self.name)

# c = C()
# print(C.__mro__)
# c.showprops()

# 8 : Interface

# Using Abstract Base Classes to implement interfaces

# from abc import ABC, abstractmethod

# class GraphicShape(ABC):
#     def __init__(self):
#         super().__init__()

#     @abstractmethod
#     def calcArea(self):
#         pass
    
# class JSONify(ABC):
#     @abstractmethod
#     def toJSON(self):
#         pass
    
# class Circle(GraphicShape, JSONify):
#     def __init__(self, radius):
#         self.radius = radius

#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)

#     def toJSON(self):
#         return f"{{'Circle': {str(self.calcArea())}}}"
    
# c = Circle(10)
# print(c.calcArea())
# print(c.toJSON())

# 9 : Composition

# Using composition to build complex objects

# class Book:
#     def __init__(self, title, price, author = None):
#         self.title = title
#         self.price = price

#         self.author = author
#         self.chapters = []

#     def addchapter(self, chapter):
#         self.chapters.append(chapter)
        
#     def getbookpagecount(self):
#         result = 0
#         for ch in self.chapters:
#             result += ch.pagecount
#         return result

# class Author:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
    
#     def __str__(self):
#         return f"{self.fname} {self.lname}"
    
# class Chapter:
#     def __init__(self, name , pagecount):
#         self.name = name
#         self.pagecount = pagecount

# auth = Author("Leo", "Tolstoy")
# b1 = Book("War and Peace", 39.0, auth)

# b1.addchapter(Chapter("Chapter 1", 125))
# b1.addchapter(Chapter("Chapter 2", 97))
# b1.addchapter(Chapter("Chapter 3", 143))

# print(b1.title)
# print(b1.author)
# print(b1.getbookpagecount())
