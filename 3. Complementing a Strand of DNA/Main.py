f = open("input.txt","r")           # Open the dataset
line = f.read()                     # Read the line in the dataset

# line = "AAAACCCGGT"
lineList = list(line)               # Transfer the string in the dataset to a list
lineList.reverse()                  # Reverse the list

dnaDict = {                         # Make a dictionary containing the complement
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C",
    "\n":""
}

newLine = ""                        # Make a new string to store the complementary DNA string
for x in lineList:
    newLine = newLine + dnaDict[x]

# if newLine == "ACCGGGTTTT":
#     print("Test passed.")

nf = open("output.txt","w")
nf.write(newLine)                   # Write the complementary DNA string in a new file
