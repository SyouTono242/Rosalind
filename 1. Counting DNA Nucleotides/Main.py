f = open("input.txt", "r")
line = f.read()

# line = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC" // Test line

A = line.count("A")
T = line.count("T")
G = line.count("G")
C = line.count("C")

print(A,C,G,T)
