# Given: A protein string P of length at most 1000 aa.
#
# Return: The total weight of P. Consult the monoisotopic mass table.

table = {}
tableFile = open("mass table.txt","r")
for line in tableFile:
    table[line[0]]=float(line[4::].strip())

aaFile = open("input.txt","r")
total = float(0)
for aa in aaFile.read().replace("\n",""):
    total += table[aa]
print("%.3f"%total)
