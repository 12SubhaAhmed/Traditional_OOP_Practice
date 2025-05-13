# # 1. Using self
# # Create a class Student with attributes name and marks.
# # Use the self keyword to initialize these values via a constructor. 
# # Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f'Student Name: {self.name}')
        print(f'Marks: {self.marks}')

student1 = Student("Subha", 80)
student1.display()


# # 2. Using cls
# # Create a class Counter that keeps track of how many objects have been created.
# # Use a class variable and a class method with cls to manage and display the count.
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def dispaly_counter(cls):
        print(f'My total objects are: {cls.count}')

obj1 = Counter()
obj2=  Counter()
obj3 = Counter()

Counter.dispaly_counter()

# # 3. Public Variables and Methods
# # Create a class Car with a public variable brand and a public method start(). 
# # Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand} is starting...!')

my_car = Car("Sonata")
print(my_car.brand)
my_car.start()

# # 4. Class Variables and Class Methods
# # Create a class Bank with a class variable bank_name. 
# # Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# # Show that it affects all instances.

class Bank:
    bank_name = "Meezan Bank"
    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f'Account Holder: {self.account_holder}, Bank: {self.bank_name}')

account1 = Bank("Ali")
account2 = Bank("Hamza")
account1.display()
account2.display()

Bank.change_bank_name("UBL Bank")
account1.display()
account2.display()


# # 5. Static Variables and Static Methods
# # Create a class MathUtils with a static method add(a, b) that returns the sum. 
# # No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
result = MathUtils.add(13,5)
print("Sum = ",result)


# # 6. Constructors and Destructors
# # Create a class Logger that prints a message when an object is created (constructor) 
# # and another message when it is destroyed (destructor).
class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed.")

log = Logger()
del log

# # 7. Access Modifiers: Public, Private, and Protected
# # Create a class Employee with:
# # a public variable name,
# # a protected variable _salary, and
# # a private variable __ssn.
# # Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Alice", 50000, "123-45-6789")

 #public variable
print("Public Name:", emp.name)

#protected variable
print("Protected _salary:", emp._salary)

try:
    print("Private __ssn:", emp.__ssn)

except AttributeError as e:
    print("Error accessing __ssn directly:", e)

print("private __ssn (by name mangling:),", emp._Employee__ssn)


# # 8. The super() Function
# # Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, 
# # add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        print(f'Person constructor called. Name: {self.name}')

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f'Teacher constructor called. Subject: {self.subject}')

teacher = Teacher("Mr.Smith", "Mathematics")

# 9. Abstract Classes and Methods
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(6,7)
print(f'Area of rectangle:', rect.area())


# 10. Instance Methods
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
       print(f'{self.name} says, Woof Woof!')

dog1 = Dog("Baddy", "Aidi")
dog1.bark()
 
#  11. Class Methods
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book("The Great Gatsby")
book2 = Book("1984")
book3 = Book("To Kill a Mockingbird")

print("Total books added:", Book.total_books)

# 12. Static Methods
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class Temperature:
    @staticmethod
    def celcius_to_fahrenheit(c):
        return(c * 9/5) + 32
    
temp_c = 25
temp_f = Temperature.celcius_to_fahrenheit(temp_c)

print(f'{temp_c}C is equal to {temp_f}F')

# 13. Composition
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "Engine has started."

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start_car(self):
        return self.engine.start()  

engine = Engine()
my_car = Car(engine)
print(my_car.start_car())

# 14. Aggregation
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f'Employee: {self.name}, ID: {self.emp_id}'
    
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_employee_info(self):
        return f"{self.dept_name} Department - {self.employee.get_details()}"

emp1 = Employee("Ali", 101)

dept = Department("IT", emp1)

print(dept.show_employee_info())

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.   

class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):
    pass

obj = D()
obj.show()

print(D.__mro__)

# 16. Function Decorators
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

# Define the decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Apply the decorator to the say_hello function
@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# 17. Class Decorators
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Define the class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of Person
person = Person("Alice")

# Call the greet method from the decorator
print(person.greet()) 

# 18. Property Decorators: @property, @setter, and @deleter
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    # Deleter for price
    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Creating an instance of Product
product = Product(100)

# Using the @property getter
print(product.price) 

# Using the @price.setter to update the price
product.price = 150
print(product.price) 

# Using the @price.setter to handle invalid price input
try:
    product.price = -50  
except ValueError as e:
    print(e)  

del product.price  

# 19. callable() and __call__()
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  
    
    # Define the __call__ method to make the object callable
    def __call__(self, value):
        return value * self.factor

multiplier = Multiplier(6)

print(callable(multiplier))  

result = multiplier(5)  
print(result)  

# 20. Creating a Custom Exception
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Define the custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check the age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age cannot be less than 18") 
    else:
        print("Age is valid")

try:
    check_age(16)  
except InvalidAgeError as e:
    print(f"Error: {e}")  

try:
    check_age(20)  
except InvalidAgeError as e:
    print(f"Error: {e}")

# 21. Make a Custom Class Iterable
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start 

    # Define __iter__() to return the iterator object (self)
    def __iter__(self):
        self.current = self.start  
        return self  

    # Define __next__() to return the next value in the countdown
    def __next__(self):
        if self.current <= 0:
            raise StopIteration 
        self.current -= 1
        return self.current + 1  

countdown = Countdown(10)
for num in countdown:
    print(num)

