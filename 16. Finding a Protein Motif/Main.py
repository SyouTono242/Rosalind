# Given: At most 15 UniProt Protein Database access IDs.
#
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of
#         locations in the protein string where the motif can be found.

import urllib.request
import re

motif = "N{P}[ST]{P}"       # N-glycosylation motif

# Read the protein ids and store the corresponding sequences in a dictionary
proteinDic = {}             # Dictionary with protein ids and sequences
f = open("input.txt","r")
myfile = f.read().split()
for protein in myfile:
    url = "http://www.uniprot.org/uniprot/"+protein+".fasta"
    response = urllib.request.urlopen(url)
    content = response.read().decode()  # encode() to change it from bytes to string
    seq = content[(content.find("SV=")+4)::]    # Find the start of the protein sequence which is 4 bits from SV=
    seq = seq.replace("\n","")
    proteinDic[protein] = seq           # Store the sequences with protein ids

# Change the motif string to fit regular expression syntax
for i in motif:
    if i == "[":
        motif = motif[:(motif.find(i)+2)]+"|"+motif[(motif.find(i)+2):]
motif = motif.replace("[","(").replace("]",")").replace("{","[^").replace("}","]")

# Find the motif in the sequence and write them in the output file
output = open("output.txt","w")
for protein, seq in proteinDic.items():
    pos = []
    for i in range(len(seq)):
        if re.match(motif,seq[i:]):
            pos.append(i+1)
    if pos:
        output.write(protein+"\n")
        for ele in pos:
            output.write(str(ele)+" ")
        output.write("\n")
