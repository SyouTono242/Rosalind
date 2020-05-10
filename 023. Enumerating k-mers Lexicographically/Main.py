# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
#
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard
#         order of symbols in the English alphabet).

Alphabet = "A B C D E F"
n = 3

def alpha_combs(alphaList, n, acc="", res=[]):
    if n==0:
        res.append(acc)
    else:
        for character in alphaList:
            alpha_combs(alphaList, n-1, acc+character, res)
    return res

alphaList = sorted(Alphabet.split())
for combs in alpha_combs(alphaList, n):
    print(combs)
