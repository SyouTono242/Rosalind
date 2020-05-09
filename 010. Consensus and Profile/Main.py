# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then
#         you may return any one of them.)

f = open("input.txt","r")
lines = f.read().split(">")
lines.remove(lines[0])
newLines = []
for string in lines:
    string = string.lstrip("Rosalind_")
    string = "".join([i for i in string if not (i.isdigit())])
    newLines.append(string.replace("\n",""))
print(newLines)

listA, listC, listG, listT = [], [], [], []
bestList = []

for i in range(len(newLines[1])):
    countA, countC, countG, countT = 0,0,0,0
    for string in newLines:
        if string[i]=="A": countA += 1
        elif string[i]=="C": countC += 1
        elif string[i]=="G": countG += 1
        else: countT += 1
    listA.append(str(countA))
    listC.append(str(countC))
    listG.append(str(countG))
    listT.append(str(countT))
    iList = [countA, countC, countG, countT]
    bestList.append(["A","C","G","T"][iList.index(max(iList))])

outputf = open("output.txt","w")
outputf.write("".join(bestList)+"\n")
outputf.write("A: "+" ".join(listA)+"\n"+"C: "+" ".join(listC)+"\n"+"G: "+" ".join(listG)+"\n"+"T: "+" ".join(listT))

