# 10 : CHALLENGE
# Challenge: create a class structure to represent stocks and bonds
# Requirements:
# -- Both stocks and bonds have a price
# -- Stocks have a company name and ticker
# -- Bonds have a description, duration, and yield
# -- You should not be able to instantiate the base class
# -- Subclasses are required to override get_description()
# -- get_description returns formats for stocks and bonds
# For stocks: "Ticker: Company -- $Price"
# For bonds: "description: duration'yr' : $price : yieldamt%"

# # ~~~~~~~~~ TEST CODE ~~~~~~~~~
# try:
#    ast = Asset(100.0)
# except:
#    print("Can't instantiate Asset!")

# msft = Stock("MSFT", 342.0, "Microsoft Corp")
# goog = Stock("GOOG", 135.0, "Google Inc")
# meta = Stock("META", 275.0, "Meta Platforms Inc")
# amzn = Stock("AMZN", 135.0, "Amazon Inc")

# us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
# us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
# us5yr = Bond(98.65, "5 Year US Treasury", 5, 4.43)
# us2yr = Bond(99.57, "2 Year US Treasury", 2, 4.98)

# print(msft.get_description())
# print(goog.get_description())
# print(meta.get_description())
# print(amzn.get_description())

# print(us30yr.get_description())
# print(us10yr.get_description())
# print(us5yr.get_description())
# print(us2yr.get_description())

# from abc import ABC, abstractmethod

# class Asset(ABC):
#     def __init__(self, price):
#         self.price = float(price)
    
#     @abstractmethod
#     def get_description(self):
#         pass

# class Stock(Asset):
#     def __init__(self, Ticker, price, Company):
#         super().__init__(price)
#         self.ticker = Ticker
#         self.company = Company
        
#     def get_description(self):
#         return f"{self.ticker} : {self.company} -- ${self.price}"  

# class Bond(Asset):
#     def __init__(self, price, Description, Duration, Yield):
#         super().__init__(price)
#         self.description = Description
#         self.duration = Duration
#         self.Yield = Yield
        
#     def get_description(self):
#         return f"{self.description} : {self.duration}yr : {self.Yield}%"
# try:
#    ast = Asset(100.0)
# except:
#    print("Can't instantiate Asset!")
   
# msft = Stock("MSFT", 342.0, "Microsoft Corp")
# goog = Stock("GOOG", 135.0, "Google Inc")
# meta = Stock("META", 275.0, "Meta Platforms Inc")
# amzn = Stock("AMZN", 135.0, "Amazon Inc")

# us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
# us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
# us5yr = Bond(98.65, "5 Year US Treasury", 5, 4.43)
# us2yr = Bond(99.57, "2 Year US Treasury", 2, 4.98)

# print(msft.get_description())
# print(goog.get_description())
# print(meta.get_description())
# print(amzn.get_description())

# print(us30yr.get_description())
# print(us10yr.get_description())
# print(us5yr.get_description())
# print(us2yr.get_description())

# 11 : Magic Methods : Strings Representation

# Using the __str__ and __repr__ magic methods
# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price

#     # TODO: use the __str__ method to return a string
#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"

#     # TODO: use the __repr__ method to return an obj representation
#     def __repr__(self):
#         return f"title = {self.title}, author = {self.author}, price = {self.price}"

# b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# print(b1)
# print(b2)
# print(str(b1))
# print(repr(b2))

# 11 : Equality and Comparison

# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price

#     # TODO: the __eq__ method checks for equality between two objects
#     def __eq__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Can't compare a book to a non-book")
#         return (self.title == value.title and 
#                 self.author == value.author and 
#                 self.price == value.price) 
        
#     # TODO: the __ge__ establishes >= relationship with another obj
#     def __ge__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Can't compare a book to a non-book")
#         return self.price >= value.price        
    
#     # TODO: the __lt__ establishes < relationship with another obj
#     def __lt__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Can't compare a book to a non-book")
#         return self.price < value.price 

# b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
# b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
# b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# # TODO: Check for equality
# # print(b1 == b3)
# # print(b1 == b2)
# # print(b1 == 42)

# # TODO: Check for greater and lesser value
# print(b2 >= b1)
# print(b2 < b1)

# # TODO: Now we can sort them too
# books = [b1, b3, b2, b4]
# books.sort()
# print([book.title for book in books])

# 12 : Attribute Class

# from typing import Any

# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price
#         self._discount = 0.1

#     # The __str__ function is used to return a user-friendly string
#     # representation of the object
#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"

#     # TODO: __getattribute__ called when an attr is retrieved. Don't
#     # directly access the attr name otherwise a recursive loop is created
    
#     def __getattribute__(self, name):
#         if name == "price":
#             p = super().__getattribute__("price")
#             d = super().__getattribute__("_discount")
#             return p - (p * d)
#         return super().__getattribute__(name)
    
#     # TODO: __setattr__ called when an attribute value is set. Don't set the attr
#     # directly here otherwise a recursive loop causes a crash
    
#     def __setattr__(self, name, value):
#         if name == "price":
#             if type(value) is not float:
#                raise ValueError("The 'price' attr must be a float")
#         return super().__setattr__(name, value) 

#     # TODO: __getattr__ called when __getattribute__ lookup fails - you can
#     # pretty much generate attributes on the fly with this method
    
#     def __getattr__(self, name):
#         return name + " is not here"

# b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# # b1.price = 38.95
# # print(b1)

# # b1.price = 40
# # print(b1)
# # b1.price = float(40)
# # print(b1)

# print(b1.randomprop)

# 13 : Callable Objects

# Using the __str__ and __repr__ magic methods

# from typing import Any

# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price

#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"

#     # TODO: the __call__ method can be used to call the object like a function
#     def __call__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

# b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# # TODO: call the object as if it were a function
# print(b1)
# b1("Anna Karenina", "Leo Tolstoy", 49.95)
# print(b1)

# CHALLENGE

# Programming challenge: add methods for comparison and equality
# Challenge: use a magic method to make stocks and bonds sortable
# Stocks should sort from low to high on price
# Bonds should sort from low to high on yield

# CHALLENGE
# Programming challenge: add methods for comparison and equality

from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def __str__(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.company = company
        self.ticker = ticker

    def __str__(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"
    
    def __lt__(self, other):
        return self.price < other.price

class Bond(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt

    def __str__(self):
        return f"{self.description}: {self.duration}yr : ${self.price} : {self.yieldamt}%"

    def __lt__(self, other):
        return self.yieldamt < other.yieldamt

stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("-----------")
for bond in bonds:
    print(bond)

