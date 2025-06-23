
file_path = r"C:\Users\Asus\Downloads\student_info.txt"

with open(file_path, "w") as file:
    file.write("Name: Kamali\n")
    file.write("Course: B.Tech\n")
    file.write("Department: IT\n")

print("File created and written successfully.")
#write
with open(file_path, "r") as file:
    content = file.read()
    print("\n Reading content:")
    print(content)

# Append 
with open(file_path, "a") as file:
    file.write("Skills: Python, SQL\n")

# Read 
with open(file_path, "r") as file:
    updated_content = file.read()
    print(" Updated content after append:")
    print(updated_content)
