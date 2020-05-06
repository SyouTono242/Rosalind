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

def find_protein(DNA):
        startList = []
        for i in range(len(DNA)):
            if DNA[i:(i+3)]=="ATG":
                startList.append(i)

        for start in startList:
                protein = ""
                j = 0
                while (start+3*j+3 <= len(DNA)) and table[DNA[(start+3*j):(start+3*j+3)]] and (table[DNA[(start+3*j):(start+3*j+3)]] != "_"):
                        protein += table[DNA[(start+3*j):(start+3*j+3)]]
                        j += 1
                if start+3*j+3 <= len(DNA):
                        print(protein)

def main():
        f = open("input.txt","r")
        DNA = "".join(f.read().split()[1::])
        find_protein(DNA)
        reverseDNA = DNA.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()[::-1]
        find_protein(reverseDNA)

main()
