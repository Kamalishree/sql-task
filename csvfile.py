# import csv

# # Step 1: Define data
# data = [
#     ["Name", "Age", "Course"],
#     ["Kamali", 21, "B.Tech"],
#     ["Ravi", 22, "B.Sc"],
#     ["Meena", 20, "BCA"]
# ]

# # Step 2: File path to save the CSV
# file_path = r"C:\Users\Asus\Downloads\students.csv"

# # Step 3: Write data to CSV
# with open(file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("students.csv file created successfully.")

# # Step 4: Read and display data from CSV
# print("\n Reading from students.csv:\n")

# with open(file_path, mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


import pandas as pd

# Step 1: Define student data
data = {
    "Name": ["Kamali", "Ravi", "Meena"],
    "Age": [21, 22, 20],
    "Course": ["B.Tech", "B.Sc", "BCA"]
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Save DataFrame to CSV
file_path = r"C:\Users\Asus\Downloads\students_pandas.csv"
df.to_csv(file_path, index=False)

print(" CSV file created using pandas.")

# Step 4: Read the CSV file and display
df_read = pd.read_csv(file_path)
print("\n Reading from CSV file:\n")
print(df_read)
