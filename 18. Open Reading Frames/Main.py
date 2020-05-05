# Given: A DNA string s of length at most 1 kbp in FASTA format.
#
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any
#         order.

table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

f = open("input.txt","r")
DNA = f.read().split()[1]
proteinList = []
start = 0
n = 0
for i in range(0,len(DNA)//3):
    aaList = []
    if DNA[(n+3*i):(n+3*i+3)]=="ATG":
        while DNA[(3*n+3*i):(3*n+3*i+3)]!=("TAA"or"TAG"or"TGA"):
            aaList.append(table[DNA[(n+3*i):(n+3*i+3)]])
            n += 1
        proteinList.append("".join(aaList))
print(proteinList)
