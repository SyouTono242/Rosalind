# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are
#        homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
#         allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
from scipy.special import comb

k, m, n = "25 22 20".split()
k = int(k)      # homozygous dominant
m = int(m)      # heterozygous
n = int(n)      # homozygous recessive

totalPop = k + m + n
totalCombos = comb(totalPop, 2)
validCombos = comb(k,2) + k*m + k*n + .5*m*n + .75*comb(m,2)
probability = validCombos/totalCombos

print("%.5f" % probability)

# Better solution
def firstLaw(k,m,n):
    N = float(k+m+n)
    return 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) )

print("%.5f" % firstLaw(25,22,20))
