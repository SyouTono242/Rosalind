# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single
#         solution.)


# Read the file and store all the DNA sequences in a list based on their length
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
DNAlist = sorted(DNAlist,key = len)

# Make a list containing all the common substrings between 1st and 2nd shortest DNA sequences
substringlist=[]
for i in range(0,len(DNAlist[0])-1):
    for j in range(0,len(DNAlist[1])-1):
        if DNAlist[0][i]==DNAlist[1][j]:
            substring = DNAlist[0][i]
            n = 1
            while DNAlist[0][i+n]==DNAlist[1][j+n] and ((i+n)<len(DNAlist[0])-1 and (j+n)<len(DNAlist[1])-1):
                substring += DNAlist[0][i+n]
                n += 1
            if len(substring)>1 and substring not in substringlist:
                substringlist.append(substring)

# Remove all the common substrings that are not found in other DNA sequences
for sub in substringlist:
    for DNA in DNAlist[3::]:
        if sub not in DNA and sub in substringlist:
            substringlist.remove(sub)
substringlist = sorted(substringlist, key=len, reverse=True)    # Sort the list from longest to shortest
print(substringlist[0])     # Print the longest common substring
