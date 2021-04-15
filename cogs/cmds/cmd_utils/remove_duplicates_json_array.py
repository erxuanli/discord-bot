import json

path = input("Enter path: ")
data = None
try:
    with open(path, "r") as file:
        data = json.load(file)
        data = list(set(data))
    with open(path, "w") as file:
        json.dump(data, file)
    print("Done")
except FileNotFoundError:
    print("File not found")

