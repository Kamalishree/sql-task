#encapsulation


class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public
        self._salary = salary  # Protected

    def get_salary(self):
        return self._salary

    def work(self):
        return f"{self.name} is working."

# Inherited class
class Developer(Employee):
    def work(self):
        return f"{self.name} is writing code."

# Polymorphism with inherited classes
class Manager(Employee):
    def work(self):
        return f"{self.name} is managing the team."

# Encapsulation enforced through getter
developer = Developer("Alice", 80000)
manager = Manager("Bob", 100000)

for employee in [developer, manager]:
    print(employee.work())  # Polymorphism in action
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


#practice problems
#prog1
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id        
        self.student_name = student_name      

    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")


student1 = Student(101, "KamaliShree")
student2 = Student(102, "Rakesh")

print("Details of Student 1:")
student1.display_details()

print("\nDetails of Student 2:")
student2.display_details()

#prog2
class Rectangle:
    def __init__(self, length, width):
        self.length = length  
        self.width = width    

    def compute_area(self):
        return self.length * self.width


rect1 = Rectangle(10, 5)

print(f"Length: {rect1.length}")
print(f"Width: {rect1.width}")
print(f"Area of Rectangle: {rect1.compute_area()}")

#prog3

class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_overtime(self, hours, rate):
        """Calculate overtime pay if hours and rate are positive."""
        if hours > 0 and rate > 0:
            overtime_pay = hours * rate
            return overtime_pay
        else:
            return 0

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Base Salary: ₹{self.salary}")
       

#prog 4
numbers = [2, 4, 6, 8]

# Find sum
total_sum = sum(numbers)

# Find product
product = 1
for num in numbers:
    product *= num

print("Sum of list:", total_sum)
print("Product of list:", product)