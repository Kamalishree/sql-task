

import pyodbc

server = r'LAPTOP-A37LO3F1'   
database = 'crime management'

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;'
)

# Create cursor and execute query
cursor = conn.cursor()
cursor.execute("SELECT TOP 3 * FROM [Victim]")

# Print rows
for row in cursor.fetchall():
    print(row)

# Cleanup
cursor.close()
conn.close()

#insert

import pyodbc

# Connection setup
server = r'LAPTOP-A37LO3F1'
database = 'crime management'

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# INSERT (exclude VictimID because it's auto-generated)
insert_query = """
INSERT INTO Victim (CrimeID, Name, ContactInfo, Injuries)
VALUES (?, ?, ?, ?)
"""

#  New victim data (assumes CrimeID exists!)
victim_data = (2, 'Rahul Prasad', 'rahulprasad@example.com', 'Fracture')

# Execute insert
cursor.execute(insert_query, victim_data)
conn.commit()
print(" New victim inserted successfully.\n")

#  View last 3 victims
cursor.execute("SELECT TOP 3 * FROM Victim ORDER BY VictimID DESC")
for row in cursor.fetchall():
    print(row)

# Clean up
cursor.close()
conn.close()

import pyodbc

# DB connection
server = r'LAPTOP-A37LO3F1'
database = 'crime management'

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# INSERT with Age
insert_query = """
INSERT INTO Victim (CrimeID, Name, ContactInfo, Injuries, Age)
VALUES (?, ?, ?, ?, ?)
"""

# Sample data
new_victim = (2, 'Nithya Raj', 'nithyaraj@example.com', 'Head Injury', 33)

cursor.execute(insert_query, new_victim)
conn.commit()
print("Victim with age inserted successfully.\n")

# Confirm it was inserted
cursor.execute("SELECT TOP 5 * FROM Victim ORDER BY VictimID DESC")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()

#update

import pyodbc

# Server and DB info
server = r'LAPTOP-A37LO3F1'
database = 'crime management'

try:
    # Establish connection
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        rf'SERVER={server};'
        rf'DATABASE={database};'
        r'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
     # --- UPDATE Victim record ---
    update_query = """
    UPDATE Victim 
    SET ContactInfo = ?, Injuries = ? 
    WHERE VictimID = ?
    """
    new_contact = "updated@example.com"
    new_injury = "Recovered"
    victim_id = 2

    cursor.execute(update_query, (new_contact, new_injury, victim_id))
    conn.commit()
    print(f" Victim ID {victim_id} updated successfully.\n")

    # --- SELECT to confirm update ---
    cursor.execute("SELECT * FROM Victim WHERE VictimID = ?", victim_id)
    updated_row = cursor.fetchone()
    print(" Updated Record:", updated_row)

except pyodbc.Error as e:
    print(" Database error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print(" Connection closed.")

#alter

import pyodbc

try:
    server = r'LAPTOP-A37LO3F1'
    database = 'crime management'

    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        rf'SERVER={server};'
        rf'DATABASE={database};'
        r'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    # Check if column 'Age' exists in 'Victim' table
    check_column_query = """
    SELECT COUNT(*) 
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_NAME = 'Victim' AND COLUMN_NAME = 'Age'
    """
    cursor.execute(check_column_query)
    column_exists = cursor.fetchone()[0]

    if column_exists:
        print("Column 'Age' already exists.")
    else:
        alter_query = "ALTER TABLE Victim ADD Age INT;"
        cursor.execute(alter_query)
        conn.commit()
        print("Column 'Age' added successfully.")

except pyodbc.Error as e:
    print("Database error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Connection closed.")


    #delete
    
    import pyodbc

try:
    # Database connection
    server = r'LAPTOP-A37LO3F1'
    database = 'crime management'

    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        rf'SERVER={server};'
        rf'DATABASE={database};'
        r'Trusted_Connection=yes;'
    )

    cursor = conn.cursor()

    # Victim ID to delete
    victim_id = 2

    # --- DELETE query ---
    delete_query = "DELETE FROM Victim WHERE VictimID = ?"
    cursor.execute(delete_query, (victim_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Victim with ID {victim_id} deleted successfully.")
    else:
        print(f"No victim found with ID {victim_id}.")

except pyodbc.Error as e:
    print("Database error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Connection closed.")
    
    #truncate
    import pyodbc

try:
    server = r'LAPTOP-A37LO3F1'
    database = 'crime management'

    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        rf'SERVER={server};'
        rf'DATABASE={database};'
        r'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    # --- TRUNCATE TABLE ---
    truncate_query = "TRUNCATE TABLE Victim"
    cursor.execute(truncate_query)
    conn.commit()

    print("All records in Victim table have been permanently deleted using TRUNCATE.")

except pyodbc.Error as e:
    print("Database error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Connection closed.")


#drop
import pyodbc

try:
   
    server = r'LAPTOP-A37LO3F1'
    database = 'crime management'

    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        rf'SERVER={server};'
        rf'DATABASE={database};'
        r'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    # --- DROP TABLE ---
    drop_query = "DROP TABLE Victim"
    cursor.execute(drop_query)
    conn.commit()

    print("Victim table has been permanently dropped from the database.")

except pyodbc.Error as e:
    print("Database error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Connection closed.")
