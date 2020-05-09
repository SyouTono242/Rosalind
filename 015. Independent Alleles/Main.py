# Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has
#        genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each
#        organism always mates with an organism having genotype Aa Bb.
#
# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree
#         (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

# Binomial distribution with AaBb as success (P = 0.25)
import math
k = 5
N = 8
P = 2**k
prob = 0
for i in range(N, P+1):
    newProb = (math.factorial(P))/(math.factorial(i)*(math.factorial(P-i)))*(0.25**i)*(0.75**(P-i))
    prob += newProb
print(round(prob,3))
