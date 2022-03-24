#!/usr/bin/env python
# coding: utf-8

# ### Classes

# ### Example 1:
# 
# Create basic Class and class instance

# In[1]:


class Student:
    
    # Variables of Student Class
    name = ""
    surname = ""
    grades = None
    
    """
        The __init__() method a special method Python runs automatically whenever 
        we create a new instance based on the Student class. Similar to the "constructor" 
        in Java
    """
    def __init__(self, name, surname):
        # "self" keyword is similar to the "this" keyword in Java.
        self.name = name
        self.surname = surname
        self.grades = []
    
    """
        Add Given grade to the grade list
        
        Parameters:
            - grade : integer value
    """
    def addGrade(self, grade):
        self.grades.append(grade)
    
    """
        Calculate mean of grades
    """
    def meanGrades(self):
        return sum(self.grades) / len(self.grades)

    
    
student1 = Student("Ali", "Yılmaz")
student2 = Student("Ayşe", "Yıldırım")

student1.addGrade(50)
student1.addGrade(70)
student1.addGrade(85)

student2.addGrade(90)
student2.addGrade(70)
student2.addGrade(85)

print(f"{student1.name} {student1.surname} mean of grades: {student1.meanGrades()}")
print(f"{student2.name} {student2.surname} mean of grades: {student2.meanGrades()}")


# In[2]:


class Student_Alternative:
    
    """
        The __init__() method a special method Python runs automatically whenever 
        we create a new instance based on the Student class. Similar to the "constructor" 
        in Java
    """
    def __init__(self, name, surname):
        # "self" keyword is similar to the "this" keyword in Java.
        self.name = name
        self.surname = surname
        self.grades = []
    
    """
        Add Given grade to the grade list
        
        Parameters:
            - grade : integer value
    """
    def addGrade(self, grade):
        self.grades.append(grade)
    
    """
        Calculate mean of grades
    """
    def meanGrades(self):
        return sum(self.grades) / len(self.grades)
        
student1 = Student_Alternative("Ali", "Yılmaz")
student2 = Student_Alternative("Ayşe", "Yıldırım")

student1.addGrade(50)
student1.addGrade(70)
student1.addGrade(85)

student2.addGrade(90)
student2.addGrade(70)
student2.addGrade(85)

print(f"{student1.name} {student1.surname} mean of grades: {student1.meanGrades()}")
print(f"{student2.name} {student2.surname} mean of grades: {student2.meanGrades()}")


# ### Example 2 - Basic Car Market Example

# In[6]:


class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.km = 0
        
    def printInfo(self):
        return f"Brand:{self.brand}, Model: {self.model}, Year: {self.year}, Km: {self.km}"


# In[7]:


class CarMarket:
    
    def __init__(self, address):
        self.address = address
        self.carList = []
    
    """
        Add given car to the carList
        
        Parameters:
            - car: Instance of Car Class
    """
    def addCar(self, car):
        self.carList.append(car)
    
    """
        Print Car List in the Car Market
    """
    def printCarList(self):
        for car in self.carList:
            print(car.printInfo())


# In[8]:


import copy
hyundai = Car("Hyundai", "Tucson", "2019")
ford = Car("Ford", "Focus", "2017")

market = CarMarket("abc street")
market.addCar(hyundai)
market.addCar(ford)

# If you want to prevent changes
# market.addCar(copy.deepcopy(ford))

market.printCarList()

ford.km = 1e5

print("\nAfter the change...\n")
market.printCarList()


# ### Example 3 - Library Borrowing System
# - There are multiple books that can be borrowed in the library.
# - There are multiple students in the library that can borrow books.
# - Each student can borrow only 3 books.
# - Each book has only one author.
# - There is only one book in each book.
# 

# In[9]:


class Book:
    
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.isBorrowing = False
    
    def printInfo(self):
        return f"Book Name: {self.name}, Author: {self.author.printInfo()}"


# In[10]:


class Author:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def printInfo(self):
        return f"{self.name}, {self. surname}"


# In[11]:


class Student:
    
    def __init__(self, fullname):
        self.fullname = fullname
        self.borrowingCount = 0
        self.borrowBookList = []
    
    """
        Add Book
        
        Parameters:
            book: Instance of Book Class
    """
    def addBook(self, book):
        if (self.borrowingCount < 3) and (book.isBorrowing == False): 
            self.borrowBookList.append(book)
            self.borrowingCount = self.borrowingCount + 1
            return True
        else:
            print("You can't borrow this book.")
            return False
    
    """
        Return Borrowing Book List
    """
    def borrowingInfo(self):
        result = ""
        for book in self.borrowBookList:
            result = result + book.printInfo() + "\n"
        return result
    


# In[12]:


class Library:
    
    def __init__(self):
        self.bookList = []
        self.studentList = []
        self.givenBookCount = 0
    
    def addBook(self, book):
        self.bookList.append(book)
    
    def addStudent(self, student):
        self.studentList.append(student)
    
    """
        Borrow the given book to the student
        
        Parameters:
            student: Borrowing Student - Student Class instance
            book: Borrowed Book - Book Class instance
    """
    def borrowBook(self, student, book):
        if student in self.studentList:
            
            if book in self.bookList:
                result = student.addBook(book)
                
                if result:
                    book.isBorrowing = True
                    self.givenBookCount = self.givenBookCount + 1
                    print(f"The {book.name} was given to the {student.fullname}.")
            else:
                print("This book is not available in the library.")
            
        else:
            print("This user not registered to this Library.")
    
    def printGivenBookList(self):
        for student in self.studentList:
            print(f"\n{student.fullname}, Borrowing Count: {student.borrowingCount}")
            print(f"Book List: {student.borrowingInfo()}")
            print("*" * 20)


# In[14]:


# Instances of Author Class
tolkien = Author("J.R.R", "Tolkien")
rowling = Author("J.K", "Rowling")
bradbury = Author("Ray", "Bradbury")
homer = Author("Homer", "")
orwell = Author("George", "Orwell")

# Instances of Book Class
book_1 = Book("Lord of The Rings", tolkien)
book_2 = Book("Harry Potter", rowling)
book_3 = Book("Fahrenheit 451", bradbury)
book_4 = Book("The Odyssey", homer)
book_5 = Book("1984", orwell)

# Instances of Student Class
ali = Student("Ali Yılmaz")
ayse = Student("Ayşe Yıldırım")


library = Library()
# Add Books to the Library
library.addBook(book_1)
library.addBook(book_2)
library.addBook(book_3)
library.addBook(book_4)
library.addBook(book_5)

# Add Students to the Library
library.addStudent(ali)
library.addStudent(ayse)

library.borrowBook(ali, book_1)
library.borrowBook(ali, book_2)
library.borrowBook(ali, book_3)
# Expected: Error, Because ali have 3 books
library.borrowBook(ali, book_4)
print("------")


library.borrowBook(ayse, book_4)
library.borrowBook(ayse, book_5)
# Expected: Error, because the book_1 has already been given to ali
library.borrowBook(ayse, book_1)

library.printGivenBookList()


# In[ ]:





# In[ ]:




