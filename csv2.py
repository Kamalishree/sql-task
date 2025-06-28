data = '''Customer,Business effective date,Address
"John","2024-06-01","No.12 | Main Street"
"Emma","2024-07-15","Apartment | #45"
"Liam","","Greenfield | Street 3"
"Olivia","2024-05-20","Rose | Villa"
'''

with open("business_data.csv", "w") as f:
    f.write(data)
import pandas as pd

# Read CSV (comma as separator, quotes handle pipe-included fields)
df = pd.read_csv("business_data.csv")

print("Before Cleaning:")
print(df)

# Remove '|' symbol from all columns
df = df.replace('|', '', regex=True)

# Drop rows with any blank (NaN) values
df = df.dropna()

# Format the 'Business effective date' to dd/mm/yyyy
df['Business effective date'] = pd.to_datetime(df['Business effective date']).dt.strftime('%d/%m/%Y')

print("\nAfter Cleaning & Formatting:")
print(df)
