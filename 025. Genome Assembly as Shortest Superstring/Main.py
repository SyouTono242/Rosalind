# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent
#        reads deriving from the same strand of a single linear chromosome).
#        The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the
#        entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their
#        length.
#
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

from Bio import SeqIO

sequences = list(SeqIO.parse("input.txt","fasta"))
for fasta in sequences:
    print(fasta.seq)
