import pyodbc

server = r'LAPTOP-A37LO3F1'   
database = 'Theatre'

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;'
)


cursor = conn.cursor()
cursor.execute("SELECT TOP 3 * FROM [Screen]")

for row in cursor.fetchall():
    print(row)


cursor.close()
conn.close()

import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=LAPTOP-A37LO3F1;'
    r'DATABASE=Theatre;'
    r'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# INSERT query
insert_user = """
INSERT INTO Usertable (name, email, phone)
VALUES (?, ?, ?)
"""

user_data = ('Maya Rao', 'maya@example.com', '6789012345')

# Execute insert
cursor.execute(insert_user, user_data)
conn.commit()

print("New user inserted successfully.")

# Optional: Show last inserted user
cursor.execute("SELECT TOP 1 * FROM Usertable ORDER BY user_id DESC")
print("Inserted Record:", cursor.fetchone())

# Clean up
cursor.close()
conn.close()

import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=LAPTOP-A37LO3F1;'
    r'DATABASE=Theatre;'
    r'Trusted_Connection=yes;'
)

cursor = conn.cursor()

update_query = """
UPDATE Usertable 
SET email = ?, phone = ? 
WHERE user_id = ?
"""

new_email = "newmaya@example.com"
new_phone = "7894561230"
target_user_id = 6

cursor.execute(update_query, (new_email, new_phone, target_user_id))
conn.commit()

print(f"User ID {target_user_id} updated successfully.")

# Optional: View the updated user
cursor.execute("SELECT * FROM Usertable WHERE user_id = ?", (target_user_id,))
print("Updated Record:", cursor.fetchone())

cursor.close()
conn.close()

import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=LAPTOP-A37LO3F1;'
    r'DATABASE=Theatre;'
    r'Trusted_Connection=yes;'
)

cursor = conn.cursor()

alter_query = """
ALTER TABLE Usertable
ADD gender VARCHAR(10);
"""

try:
    cursor.execute(alter_query)
    conn.commit()
    print("Column 'gender' added to Usertable.")
except pyodbc.Error as e:
    print("Error:", e)

cursor.close()
conn.close()

import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=LAPTOP-A37LO3F1;'
    r'DATABASE=Theatre;'
    r'Trusted_Connection=yes;'
)

cursor = conn.cursor()

delete_query = """
DELETE FROM Usertable WHERE user_id = ?
"""

user_id_to_delete = 6

cursor.execute(delete_query, (user_id_to_delete,))
conn.commit()

if cursor.rowcount > 0:
    print(f"User ID {user_id_to_delete} deleted successfully.")
else:
    print(f"No user found with ID {user_id_to_delete}.")

cursor.close()
conn.close()
