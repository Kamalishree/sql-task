#list
a=[1,2,3,4,5,6]
print(a)


#append

a=[1,2,3,4,5,6]
a.append(7) 
a.append("emc")
a.append("True")
print(a)  

#insert
a=[1,2,3,4]
a.insert(0,11)
print(a[0])
print(a)

#pop
a=[1,2,3,4,5]
a.pop(2)
print(a)

#extend
a=[1,2,3,4]
b=[5,6]
a.extend(b)
print(a)

#List: Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry", "apple"]
print("Original:", fruits)

fruits.append("date")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits[1] = "blueberry"
print("After modify:", fruits)

print("Iterate:")
for f in fruits:
    print("-", f)

#tuple


# Tuple: Ordered, immutable, allows duplicates
point = (3, 4)
print("Tuple:", point)

# # Access elements
print("x =", point[0], ", y =", point[1])

# # Concatenate or repeat
t2 = point + (5,)
print("Concat:", t2)

t3 = point * 2
print("Repeat:", t3)

# Iterate
print("Iterate tuple:")
for coord in point:
    print(coord)


#Set: Unordered, mutable, unique items

nums = {1, 2, 3, 2}
print("Initial (no duplicates):", nums)

nums.add(4)
print("After add:", nums)

nums.discard(2)
print("After discard:", nums)

print("Membership test: 3 in nums?", 3 in nums)

print("Iterate set:")
for n in nums:
    print(n)

# Set operations
A = {1, 2, 3}
B = {2, 3, 4}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)

# Dictionary: Mutable mapping of unique keys → values
person = {"name": "Alice", "age": 30}
print("Original:", person)

person["age"] = 31          # Modify
person["city"] = "Chennai"  # Add
print("Updated:", person)

print("Access:", person["name"])
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

print("Iterate items:")
for k, v in person.items():
    print(f"{k} ➜ {v}")

removed = person.pop("city")
print("Popped city:", removed)
print("After pop:", person)


#1. List of student name-tuples
students = [("Alice", 85), ("Bob", 92), ("Cara", 78), ("Bob", 75)]
print("All students:", students)

#2. Use set to get unique student names
names = {name for name, _ in students}
print("Unique names:", names)

#3. Aggregate and compute average in a dict
grades = {name: [] for name in names}
for name, score in students:
    grades[name].append(score)

avg_scores = {name: sum(scores)/len(scores) for name, scores in grades.items()}
print("Average scores:", avg_scores)

#4. Identify top performers (average >= 85)
top_students = [name for name, avg in avg_scores.items() if avg >= 85]
print("Top students:", top_students)

#Voter Tracking System

#Step 1: list of people showing up in order
visitors = ["Jim", "Bob", "Alice", "Bob", "Dave", "Eve"]
print("Visitors:", visitors)

#Step 2: set to record unique voters
voted = set()
for person in visitors:
    if person in voted:
        print(f"{person} - ALREADY VOTED")
    else:
        print(f"{person} - CAST VOTE")
        voted.add(person)

print("Total voters:", len(voted))
print("Voters list:", voted)

#find longest string, filter numbers, detect duplicates

def find_longest_string(strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

def filter_greater_than_five(nums):
    return [n for n in nums if n > 5]

def find_duplicates(values):
    seen, duplicates = set(), []
    for v in values:
        if v in seen:
            duplicates.append(v)
        else:
            seen.add(v)
    return duplicates


words = ["hi", "hello", "world!"]
numbers = [1, 6, 8, 3, 4, 8]
mix = [2, 3, 2, 5, 3]

print("Longest word:", find_longest_string(words))
print("Filtered (>5):", filter_greater_than_five(numbers))
print("Duplicates in mix:", find_duplicates(mix))


#functions in python
#class and objects
class laptop:
    price="1233"
    processor="I3"
    RAM="9GB"
    
dell=laptop()
dell.price=12000
print(dell.price)
dell.processor="I7"
print(dell.processor)
dell.RAM="5GB"
print(dell.RAM)

#Company Class with Property Validation
#Manages employee count using getters, setters, and class methods:

class Company:
    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    num_employees = 100

    @classmethod
    def productivity(cls):
        return cls.turnover / cls.num_employees

c = Company()
print("Productivity:", Company.productivity())



class EmployeeManager:
    def __init__(self):
        self.employees = []  # List to store employee dictionaries

    def add_employee(self, emp_id, name, salary):
        """Adds a new employee."""
        self.employees.append({"id": emp_id, "name": name, "salary": salary})
        print(f"Employee {name} added.")

    def get_employee(self, emp_id):
        """Fetch employee details by ID."""
        for employee in self.employees:
            if employee["id"] == emp_id:
                return employee
        return f"No employee found with ID {emp_id}"

    def get_high_salary_employees(self, min_salary):
        """Filter employees with a salary above the threshold."""
        return [emp for emp in self.employees if emp["salary"] > min_salary]

# Using the class
manager = EmployeeManager()
manager.add_employee(1, "Chara", 50000)
manager.add_employee(2, "Bala", 60000)
manager.add_employee(3, "Vishnu", 40000)

print(manager.get_employee(2)) 
high_salary = manager.get_high_salary_employees(45000)
print(high_salary)  # 


class Inventory:
    def __init__(self):
        self.products = {} 
    def add_product(self, product_id, name, quantity, price):
        """Adds or updates a product."""
        if product_id in self.products:
            self.products[product_id]["quantity"] += quantity
            print(f"Updated {name}: New quantity is {self.products[product_id]['quantity']}")
        else:
            self.products[product_id] = {"name": name, "quantity": quantity, "price": price}
            print(f"Added product: {name}")

    def get_product(self, product_id):
        """Get details of a specific product."""
        return self.products.get(product_id, "Product not found")

    def get_low_stock(self, threshold):
        """Get products with stock below a threshold."""
        return {pid: data for pid, data in self.products.items() if data["quantity"] < threshold}

# Using the class
inventory = Inventory()
inventory.add_product(101, "Laptop", 10, 70000)
inventory.add_product(102, "Mouse", 50, 500)
inventory.add_product(103, "Keyboard", 5, 1500)

print(inventory.get_product(102))  # Output: {'name': 'Mouse', 'quantity': 50, 'price': 500}
low_stock = inventory.get_low_stock(10)
print(low_stock)  # Output: {103: {'name': 'Keyboard', 'quantity': 5, 'price': 1500}}

class Library:
    def __init__(self):
        self.books = []  # List of dictionaries: [{"title": str, "author": str, "available": bool}]

    def add_book(self, title, author):
        """Add a new book to the library."""
        self.books.append({"title": title, "author": author, "available": True})
        print(f"Book '{title}' added.")

    def borrow_book(self, title):
        """Borrow a book if available."""
        for book in self.books:
            if book["title"] == title:
                if book["available"]:
                    book["available"] = False
                    print(f"You borrowed '{title}'")
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found.")

    def get_available_books(self):
        """List all available books."""
        return [book for book in self.books if book["available"]]

# Using the class
library = Library()
library.add_book("Python Programming", "Madan")
library.add_book("Data Structures", "Bala")

library.borrow_book("Python Programming")  # Output: You borrowed 'Python Programming'
print(library.get_available_books())  # 

class Product:
    """Base class to represent a product."""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_details(self):
        """Get product details."""
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}"

class Sales:
    """Class to track sales of products."""
    def __init__(self):
        self.sales = []  # List to store sales records

    def add_sale(self, product, quantity):
        """Add a sale record."""
        total_price = product.price * quantity
        self.sales.append({"product": product, "quantity": quantity, "total_price": total_price})
        print(f"Sale added: {product.name} x {quantity} for {total_price}")

    def get_total_sales(self):
        """Calculate total sales amount."""
        return sum(sale["total_price"] for sale in self.sales)

    def get_sales_report(self):
        """Generate sales report."""
        report = "Sales Report:\n"
        for sale in self.sales:
            report += f"{sale['product'].name}: {sale['quantity']} units - {sale['total_price']} total\n"
        return report


# Main program
if __name__ == "__main__":
    # Create products
    product1 = Product(1, "Laptop", 70000)
    product2 = Product(2, "Smartphone", 30000)

    # Create sales tracker
    sales_tracker = Sales()

    # Add sales
    sales_tracker.add_sale(product1, 3)
    sales_tracker.add_sale(product2, 5)

    # Display sales report and total sales
    print("\n" + sales_tracker.get_sales_report())
    print(f"Total Sales: {sales_tracker.get_total_sales()}")



