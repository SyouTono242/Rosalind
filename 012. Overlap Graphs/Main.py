# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
#
# Return: The adjacency list corresponding to O3. You may return edges in any order.

# this method makes a dictionary from FASTA format DNA strings
def makedict(filename):
    fastadict = {}
    for line in filename:
        if line[0] == ">":
            key = line.split()[0].replace(">","")
            fastadict[key] = ""
        else:
            fastadict[key] += line.strip()
    return fastadict

filename = open("input.txt","r")
fastadict = makedict(filename)

outputFile = open("output.txt","w")

for headkey in fastadict:
    head = fastadict[headkey][0:3]
    for tailkey in fastadict:
        tail = fastadict[tailkey][-3::]
        if tail == head and headkey != tailkey:
            outputFile.write(tailkey+" "+headkey+"\n")
