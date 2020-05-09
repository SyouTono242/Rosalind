import os

print("The directory is: %s"%os.listdir(os.getcwd()))

for directory in os.listdir(os.getcwd()):
    if directory[0].isdigit():
        os.rename(directory, "0"+directory)
