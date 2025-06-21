# print hello world:

print("hello world")
n=10
print(n)
v="nfkjrnf"

# using type function:

a=20.3
print(type(n),type(a),n,a)
print(v,type(v))

# local variables and outer variables
if(n==10):
    print("matched")
else:
    print("not matched")
def fun():
    a=30.0
    print(a)
fun()
print(a)

#To print datatype

p="rnjr"
print(type(p),p)

kx=19>23
print(type(kx),kx)

pp=5+6j
print(type(pp),pp)

#if statement 
val=int(input("Enter number:"))
if(val%10==0):
    print(val,"data")
else:
    print("pata")

#using fstring :

val=int(input("Enter number:"))
if(val%10==0):
    print(f"{val} data")
elif(val%20==0):
    print("tata")
else:
    print("pata")
    

# checking prime number:

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.") 


#Program: Even or Odd Checker for a List

# List of numbers
numbers = [10, 15, 22, 33, 40, 55]

# Loop through each number in the list
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


#Program: Using else after a loop

for i in range(1, 4):
    print(f"Checking i = {i}")
    if i == 5:
        print("Found 5! Breaking the loop.")
        break
else:
    print("Loop finished without break.")
    
    x = int(input("Enter a number: "))

if x > 10:
    print("x is greater than 10")
    
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is greater than 10 but not greater than 20")
else:
    print("x is 10 or less")


age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ").lower()

if age >= 18 and has_license == "yes":
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")

ages = [78, 34, 21, 47, 9]
condition = True

if condition:
    for age in ages:
        if age < 18:
            print(f"Age {age} is a minor.")
        else:
            print(f"Age {age} is an adult.")
else:
    print("Condition is off.")


num = int(input("Enter a number to find factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} is {fact}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to find factorial (recursive): "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")


n = int(input("Enter how many Fibonacci numbers to print: "))

if n <= 0:
    print("Enter a positive number.")
elif n == 1:
    print("0")
else:
    a, b = 0, 1
    print("Fibonacci sequence:")
    print(a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c


#classand objects

class employee:
    def __init__(self):
        self.employee={}
    def addemployee(self,employeeid,name,department,salary):
        if employeeid in self.employee:
            print(f"{employeeid} already exists")
        else:
            self.employee[employeeid]={"name":name,"department":department,"salary":salary}
    def displayemployee(self):
        print(self.employee)
    
    def highestsalary(self):
        list=[]
        for i,data in self.employee.items():
            list.append(data["salary"])
        maximum_salary=max(list)
        for i,data in self.employee.items():
            if data["salary"]==maximum_salary:
                print(i,":",data)
    def calhighcondition(self, condition):
        result = [
            {
            "emp_id": emp_id,
            "name": data["name"],
            "department": data["department"],
            "salary": data["salary"]
            }
            for emp_id, data in self.employee.items()
            if data["salary"] > condition
            ]
        print(result)

em = employee()
empdata= [
    {"emp_id": 101, "name": "Alice", "department": "HR", "salary": 50000},
    {"emp_id": 102, "name": "Bob", "department": "IT", "salary": 75000},
    {"emp_id": 103, "name": "Charlie", "department": "Finance", "salary": 60000},
    {"emp_id": 104, "name": "Diana", "department": "IT", "salary": 82000}
]
for i in empdata:
    em.addemployee(i["emp_id"],i["name"],i["department"],i["salary"])
em.displayemployee()
em.highestsalary()
em.calhighcondition(60000)


# Inventory management

class inventory:
    def __init__(self):
        self.product={}
        
    def addproducts(self,pro_id,name,quantity,price):
        self.product[pro_id]={"name":name,"quantity":quantity,"price":price}
        
    def displayproduct(self):
        for i,j in self.product.items():
            print(i,":",j)
        
    #updating the quantity in the product
    
    def updatequantity(self, quantity, product_id):
        if product_id in self.product:
            self.product[product_id]["quantity"] += quantity
            print(f"Quantity updated. New quantity: {self.product[product_id]['quantity']}")
        else:
            print("No such product ID exists.")
    
    def getspecificpro(self,pro_id):
        if pro_id in self.product:
            print(self.product[pro_id])
        else:
            print("No such product ID exists.")
        
    def getlowstock(self,quantity):
        list=[{"pro_id":pro_id,"name":data["name"],"quantity":data["quantity"],"price":data["price"] }
              for pro_id,data in self.product.items() if data["quantity"]<quantity]
        for i in list:
            print(i)
        


inn=inventory()
product_data = [
    {"pro_id": 201, "name": "Laptop", "quantity": 10, "price": 55000},
    {"pro_id": 202, "name": "Smartphone", "quantity": 25, "price": 20000},
    {"pro_id": 203, "name": "Headphones", "quantity": 50, "price": 1500},
    {"pro_id": 204, "name": "Monitor", "quantity": 15, "price": 12000},
    
]
for i in product_data:
    inn.addproducts(i["pro_id"],i["name"],i["quantity"],i["price"])
inn.updatequantity(55,203)
inn.displayproduct()
inn.getspecificpro(204)
inn.getlowstock(20)

class Library:
    def __init__(self):
        self.books = []

    def addbook(self, title, author):
        self.books.append({"title": title, "author": author, "available": True})
        print(f"Book '{title}' by {author} added to the library.")

    def borrowbook(self, title):
        for book in self.books:
            if book["title"] == title:
                if book["available"]:
                    book["available"] = False
                    print(f"You borrowed '{title}'.")
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found in the library.")

    def getavailablebooks(self):
        return [book for book in self.books if book["available"]]

    def displayavailablebooks(self):
        available = self.getavailablebooks()
        if not available:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available:
                print(f"- {book['title']} by {book['author']}")

library=Library()
library.addbook("The Alchemist", "Paulo Coelho")
library.addbook("Clean Code", "Robert C. Martin")
library.addbook("Introduction to Algorithms", "Cormen")
library.addbook("The Psychology of Money", "Morgan Housel")
library.addbook("To Kill a Mockingbird", "Harper Lee")

print()
library.borrowbook("Clean Code")
library.borrowbook("The Alchemist")
library.borrowbook("To Kill a Mockingbird")

print()

# library.displayavailablebooks()

class product1:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
    def display(self):
        print(f"{self.product_id},{self.name},{self.price}")
class sales:
    def __init__(self):
        self.sale=[]
    def addsale(self,product1,quantity):
        price=quantity* product1.price
        self.sale.append({"product_id":product1.product_id,"name":product1.name,"total_price":price})
        print(self.sale)
    def totalsale(self):
        print("Total_sum = ",sum(data["total_price"] for data in self.sale))
    def report(self):
        for i in self.sale:
            print(i)
if __name__ == "__main__":
    
    prod1=product1(101,"mobile",70000)
    prod2=product1(102,"airpods",60000)
    
    sale1=sales()
    sale1.addsale(prod1,25)
    sale1.addsale(prod2,40)
    
    prod1.display()
    sale1.totalsale()
    sale1.report()
            
#encapsulation

class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
        
    def get_salary(self):
        return self._salary

    def work(self):
        return f"{self.name} is working."

class Developer(employee):
    def work(self):
        return f"{self.name} is writing code."

class Manager(employee):
    def work(self):
        return f"{self.name} is managing the team."

developer = Developer("Alice", 80000)
manager = Manager("Bob", 100000)

for employee in [developer, manager]:
    print(employee.work())  
    print(f"{employee.name}'s salary: {employee.get_salary()}")


class BankAccount:
    """Base class for a generic bank account."""
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute

    # Encapsulated method to access private balance
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        """Withdraw money from the account (to be overridden)."""
        raise NotImplementedError("Withdraw method must be implemented by subclasses.")

    def get_account_info(self):
        """Return account information (to be overridden)."""
        raise NotImplementedError("get_account_info method must be implemented by subclasses.")

# Savings Account class
class SavingsAccount(BankAccount):
    """Savings account with interest and minimum balance."""
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate  # Public attribute

    def withdraw(self, amount):
        """Savings account allows withdrawal only if balance >= 500 after withdrawal."""
        if self.get_balance() - amount >= 500:
            # Access private balance using deposit method to decrease balance
            self.deposit(-amount)  # Using negative deposit to reduce balance
            print(f"{amount} withdrawn from Savings Account.")
        else:
            print("Insufficient balance! Minimum balance of 500 must be maintained.")

    def calculate_interest(self):
        """Add interest to the account balance."""
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added.")

    def get_account_info(self):
        return f"SavingsAccount: Holder: {self.account_holder}, Balance: {self.get_balance()}"

# Current Account class
class CurrentAccount(BankAccount):
    """Current account with overdraft facility."""
    def __init__(self, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Current account allows withdrawal even if balance goes negative, up to overdraft limit."""
        if self.get_balance() - amount >= -self.overdraft_limit:
            self.deposit(-amount)  # Using negative deposit to reduce balance
            print(f"{amount} withdrawn from Current Account.")
        else:
            print("Exceeded overdraft limit!")

    def get_account_info(self):
        return f"CurrentAccount: Holder: {self.account_holder}, Balance: {self.get_balance()}"

# Main program demonstrating all concepts
def main():
    # Create accounts
    savings = SavingsAccount("Vishnu", balance=2000, interest_rate=0.04)
    current = CurrentAccount("Vishwa", balance=500, overdraft_limit=1000)

    # Polymorphism: Different behaviors for the same method
    accounts = [savings, current]

    for account in accounts:
        print("\n" + account.get_account_info())
        account.deposit(500)
        account.withdraw(1000)

        if isinstance(account, SavingsAccount):
            account.calculate_interest()  # Specific to SavingsAccount

    print("\nFinal Account Information:")
    for account in accounts:
        print(account.get_account_info())

if __name__ == "__main__":
    main()

# Create a Student class with student_id and student_name, then instantiate and display their values

class rectangle:
    def area(self,length,breadth):
        return length* breadth
rr=rectangle()
length=int(input("Enter length:"))
breadth=int(input("Enter breadth:"))
print(f" the area is {rr.area(length,breadth)}")

# Student Class with Instance Attributes 
# Create a Student class with student_id and student_name, then instantiate and display their values

class student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def display(self):
        print(f"studentid: {self.student_id} , studentname: {self.student_name}")
st = student(101,"kamali")
st.display()

# Implement a class with attributes like emp_id, name, salary, department, and method to calculate overtime pay

class employee:
    def __init__(self,emp_id,name,dept,salary=0):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.salary=salary
    def calculateovertime(self,overtimehour,overtimerate):
        self.salary+=overtimehour*overtimerate
        print(f"{self.emp_id} {self.name} {self.dept} {self.salary}")
em=employee(101,"kamali","cse")
em.calculateovertime(30,300)

# Find the Sum & Product of a List/ Do the String Reversal

class product:
    def __init__(self):
        self.list=[]
    def adddata(self,data):
        self.list.append(data)
    def displaylist(self):
        print(self.list)
    def sumlist(self):
        print(sum(self.list))
    def productlist(self):
        product=1
        for i in self.list:
            product*=i
        print(product)
    def reversestring(self,str):
        print(str[::-1])
p=product()
for i in range(1,6):
    p.adddata(i)
p.displaylist()
p.sumlist()
p.productlist()
p.reversestring("kamali")
