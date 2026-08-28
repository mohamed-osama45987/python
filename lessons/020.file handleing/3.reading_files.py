# will read txt , json and csv files
file_path = "./generated files/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File is not found")
except PermissionError:
    print("You do not have permisson to read this file")
except Exception:
    print("Somthing went wrong")


# for json
file_path = "./generated files/output.json"
import json

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        # it gives you a valid json obj you can access it with the key of the obj
        print(content["age"])
except FileNotFoundError:
    print("File is not found")
except PermissionError:
    print("You do not have permisson to read this file")
except Exception:
    print("Somthing went wrong")


# for csv

# will read txt , json and csv files
file_path = "./generated files/output.csv"
import csv

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File is not found")
except PermissionError:
    print("You do not have permisson to read this file")
except Exception:
    print("Somthing went wrong")
