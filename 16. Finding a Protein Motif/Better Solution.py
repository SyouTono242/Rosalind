#!/usr/bin/env python
from re import finditer
from sys import argv
from urllib.request import urlopen

uniprot = "http://www.uniprot.org/uniprot/%s.fasta"

for protein in open("input.txt", 'r').read().strip().splitlines():

    # Fetch the protein's fasta file and get rid of newlines.'
    f = urlopen(uniprot % protein).read().decode('utf-8')
    f = ''.join(f.splitlines()[1:])

    # Find all the positions of the N-glycosylation motif.
    locs = [g.start()+1 for g in finditer(r'(?=N[^P][ST][^P])', f)]

    # Print them out, if any.
    if locs:
        print(protein)
        print(' '.join(map(str, locs)))
