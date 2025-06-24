

#Error handling

import json

try:
    with open(r"C:\Users\Asus\Downloads\basic.json", 'r') as file:
        data = json.load(file)

except FileNotFoundError:
    print("The file was not found.")

except json.JSONDecodeError:
    print(" Invalid JSON format.")

else:
    print("JSON loaded successfully:")
    print(data)

finally:
    print("JSON read attempt finished.")


