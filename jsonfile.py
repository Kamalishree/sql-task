import json

# Step 1: Define student data
student = {
    "name": "Kamali",
    "age": 21,
    "course": "B.Tech",
    "skills": ["Python", "SQL"]
}

# Step 2: Save to a JSON file
file_path = r"C:\Users\Asus\Downloads\student.json"

with open(file_path, 'w') as file:
    json.dump(student, file, indent=4)

print("Student data saved successfully!")

# Step 3: Read back the file
with open(file_path, 'r') as file:
    result = json.load(file)

print("Student Data:")
print(result)
