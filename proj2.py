import datetime
import math

def get_grade(marks):
    return 'A' if marks >= 90 else ('B' if marks >= 75 else 'C' if marks >= 60 else 'D')

students = {
    "John": [85, 90, 78],
    "Alice": [92, 88, 95],
    "Bob": [65, 70, 60]
}

report_card = {}
for student, marks in students.items():
    total = sum(marks)
    avg = round(total / len(marks), 2)
    grade = get_grade(avg)
    report_card[student] = {
        'Total': total,
        'Average': avg,
        'Grade': grade,
        'Date': datetime.date.today().strftime("%d-%m-%Y")
    }

# Lambda to find topper
topper = max(report_card.items(), key=lambda item: item[1]['Average'])

print("Report Card:", report_card)
print("Topper:", topper)
