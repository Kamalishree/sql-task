import math
import datetime

def add_expense(expenses, category, amount):
    date = datetime.date.today().strftime("%Y-%m-%d")
    expenses.append((date, category, amount))

def monthly_summary(expenses):
    summary = {}
    for date, category, amount in expenses:
        month = date[:7]
        summary[month] = summary.get(month, 0) + amount
    return summary

# Sample usage
expenses = []
add_expense(expenses, 'Food', 500)
add_expense(expenses, 'Rent', 2000)
add_expense(expenses, 'Transport', 300)

print("All Expenses:", expenses)
print("Monthly Summary:", monthly_summary(expenses))
