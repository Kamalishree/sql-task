



# print("hello world")
# n=10
# print(n)


# # using type function:

# v = "nfkjrnf" 
# a=20.3
# print(type(n),type(a),n,a)
# print(v,type(v))

# # local variables and outer variables
# if(n==10):
#     print("matched")
# else:
#     print("not matched")
   
# def fun1():
#     b=10
#     print(b)
# fun1()

    
# def fun():
#     a=30.0
#     print(a)
# fun()
# print(a)

# #To print datatype

# p="rnjr"
# print(type(p),p)

# kx=19>23
# print(type(kx),kx)

# pp=5+6j
# print(type(pp),pp)

#if statement 
# val=int(input("Enter number:"))
# if(val%10==0):
#     print(val,"data")
    
# else:
#     print("not a data")

#using fstring :

# val=int(input("Enter number:"))
# if(val%10==0):
#     print(f"{val} data")
# elif(val%20==0):
#     print("tata")
# else:
#     print("not a data")
    

# #checking prime number:

# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")


    
# numbers = [10, 15, 22, 33, 40, 55]

# # Loop through each number in the list
# for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} is even")
        
        
#     else:
#         print(f"{num} is odd")


# for i in range(1, 4):
#     print(f"Checking i = {i}")
#     if i == 5:
#         print("Found 5! Breaking the loop.")
#         break
# else:
#     print("Loop finished without break.")

# for i in range(1, 6):
#     print(f"Checking i = {i}")
#     if i == 6:
#         print("Found 3! Breaking the loop.")
#         break
# else:
#     print("Loop finished without break.")



# x = int(input("Enter a number: "))

# if x > 10:
#     print("x is greater than 10")
    
#     if x > 20:
#         print("x is also greater than 20")
#     else:
#         print("x is greater than 10 but not greater than 20")
# else:
#     print("x is 10 or less")

    
# # 
# age = int(input("Enter your age: "))
# has_license = input("Do you have a driving license? (yes/no): ")

# if age >= 18 and has_license == "yes":
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.")
    
# condition = True

# if condition:
#     for age in ages:
#         if age < 18:
#             print(f"Age {age} is a minor.")
#         else:
#             print(f"Age {age} is an adult.")
# else:
#     print("Condition is off.")

# num = int(input("Enter a number to find factorial: "))

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     print(f"Factorial of {num} is {fact}")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a number to find factorial (recursive): "))

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"Factorial of {num} is {factorial(num)}")

# n = int(input("Enter how many Fibonacci numbers to print: "))

# if n <= 0:
#     print("Enter a positive number.")
# elif n == 1:
#     print("0")
# else:
#     a, b = 0, 1
#     print("Fibonacci sequence:")
#     print(a, b, end=" ")
#     for _ in range(2, n):
#         c = a + b
#         print(c, end=" ")
#         a, b = b, c

#String Functions:

# Clean and normalize a name:
raw = "   Kamali "
clean = raw.strip().title()
print(clean)  # "John Doe"

# Count vowels:
s = "hello world"
vowels = sum(s.count(v) for v in "aeiou")
print(vowels)  # 3

# Replace digits with '*' using translate():
import string
tbl = str.maketrans({d: "*" for d in string.digits})
print("Phone: 123-456".translate(tbl))  # Phone: ***-***

# Join words with comma:
words = ["apple", "banana", "cherry"]
print(", ".join(words))  # apple, banana, cherry

# Using f-string for formatting:
name, age = "Alice", 30
print(f"{name.upper()} is {age} years old.")
