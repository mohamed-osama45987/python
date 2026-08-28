txt_data = "I like food"

base_path = "./generated files"

# can be any path for relative or abs path
file_path = base_path + "/output.txt"

# w is write and will overwride it exists
# x is to make the file if does not exist will error if file already exists
# a is to append if file exists
# r is to read file
try:
    with open(file_path, "w") as file:
        file.write(txt_data)
        print(f"Txt file generated at {file_path}")
except FileExistsError:
    print("That file already exists")


# if you want to make a json file

import json

employee = {"name": "Mo", "age": 30, "Job": "Programmer"}

file_path = base_path + "/output.json"

try:
    with open(file_path, "w") as file:
        # dump is to change json to jsom string
        json.dump(employee, file, indent=4)
        print(f"Json file generated at {file_path}")
except FileExistsError:
    print("That file already exists")


# to make a csv file

import csv

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patric", 37, "Unempolyed"],
    ["Sandy", 27, "Scientist"],
]
file_path = base_path + "/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for employee in employees:
            writer.writerow(employee)
        print(f"Csv file generated at {file_path}")
except FileExistsError:
    print("That file already exists")
