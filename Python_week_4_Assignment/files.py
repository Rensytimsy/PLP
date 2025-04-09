# Handling files in python, methods open, close, read, write
"""File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read. """


# The function below simply reads a file and returns its contents
def ReadFileFun(file_name):
    if file_name:
        try: 
            with open(file_name, "r") as file:
                data = file.read()
                print(data)
        except FileNotFoundError:
            print("Pleas provide a file")

# The function below updates files content when invoked

def UpdateFile(file_name):
    if file_name:
        try:
            with open(file_name, 'w') as file:
                data = file.write("Hello world this the updated content wow!")
                print(data)

        except FileNotFoundError:
            print("Please provide a file")
        

ReadFileFun("testfile.txt")