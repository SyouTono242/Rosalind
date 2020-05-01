# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single
#         solution.)


f = open("input.txt","r")
DNAlist = []
currDNA = ""
for line in f:
    if line[0] == ">":
        DNAlist.append(currDNA)
        currDNA = ""
    else:
        currDNA += line.strip()
DNAlist.append(currDNA)
DNAlist.remove("")

