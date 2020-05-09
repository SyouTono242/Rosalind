f = open("input.txt","r")
line = f.read()

# line = "GATGGAACTTGACTACGTAAATT"

newLine = line.replace("T","U")
print(newLine)


# sampleOutput = "GAUGGAACUUGACUACGUAAAUU"
# if newLine == sampleOutput:
#     print("Test passed.")
