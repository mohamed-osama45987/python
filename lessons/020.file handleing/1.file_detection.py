# note in the terminal you need to be at the current diretory for this to work
import os

# can be relative path or absoulte
file_path = "./0.test.txt"

if os.path.exists(file_path):
    print(
        "File exists",
    )
    # use isFile and isdir to know if it is a file or dir
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a dir")
else:
    print("File does not exist")
