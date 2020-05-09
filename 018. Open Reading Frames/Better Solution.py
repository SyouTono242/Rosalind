import re

pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')

# return the reverse compliment DNA
def revcomp(DNA):
    return DNA.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()[::-1]

# Translate the given DNA to amino acid string
def translate(DNA):
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
    protein =""
    if len(DNA)%3 == 0:
        for i in range(0, len(DNA), 3):
            codon = DNA[i:i + 3]
            protein+= table[codon]
    return protein

# Find the open reading frame of original and reverse compliment DNA and return a list of protein translated
def orfs(DNA):
    proteinList = []
    for i in set(pattern.findall(DNA)+ pattern.findall(revcomp(DNA))):
        proteinList.append(translate(i))
    return proteinList

# Main
f = open("input.txt","r")
DNA = "".join(f.read().split()[1::])
for i in orfs(DNA):
    print(i)
