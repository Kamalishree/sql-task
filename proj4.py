#Simple Bill Splitter
import math

def split_bill(people, total_amount):
    per_person = math.ceil(total_amount / len(people))
    return list(map(lambda name: (name, per_person), people))

names = ['Anu', 'Bala', 'Cathy', 'Dinesh']
total = 1234

result = split_bill(names, total)
for name, amount in result:
    print(f"{name} has to pay ₹{amount}")
