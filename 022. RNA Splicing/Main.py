# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings
#        are given in FASTA format.
#
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will
#         exist for the dataset provided.)

from Bio import SeqIO, Seq

sequences = list(SeqIO.parse("input.txt","fasta"))
DNA = str(sequences[0].seq)
for i in range(1,len(sequences)):
    DNA = DNA.replace((str(sequences[i].seq)),"")
print(Seq.translate(DNA)[:-1])
