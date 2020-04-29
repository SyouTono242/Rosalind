# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
#         for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute
#         error below.

lines = ""
DNAdict = {}


infile = open("input.txt","r")
for line in infile:
    lines = lines + line.strip("\n")
DNAlines = lines.split(">")
DNAlines.pop(0)

for DNA in DNAlines:
    DNAdict[DNA[0:13]] = round(((DNA[13::].count("G")+DNA[13::].count("C"))/len(DNA[13::]))*100,6)

print(max(DNAdict, key = DNAdict.get))
print(DNAdict[max(DNAdict, key = DNAdict.get)])
