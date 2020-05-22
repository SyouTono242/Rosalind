# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent
#        reads deriving from the same strand of a single linear chromosome).
#        The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the
#        entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their
#        length.
#
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

from Bio import SeqIO

def find_overlaps(arr, acc=""):
    if len(arr)==0:
        return acc
    elif len(acc)==0:
        acc = arr.pop(0)
        return find_overlaps(arr,acc)
    else:
        for i in range(len(arr)):
            curr_seq = arr[i]
            curr_len = len(curr_seq)
            for p in range(curr_len//2):
                suffix = curr_len-p
                if acc.startswith(curr_seq[p:]):
                    arr.pop(i)
                    return find_overlaps(arr,curr_seq[:p]+acc)
                if acc.endswith(curr_seq[:suffix]):
                    arr.pop(i)
                    return find_overlaps(arr, acc+curr_seq[suffix:])


sequences = list(SeqIO.parse("rosalind_long.txt","fasta"))
reads = [str(DNA.seq) for DNA in sequences]
print(find_overlaps(reads))
