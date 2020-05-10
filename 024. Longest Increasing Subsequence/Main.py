# Given: A positive integer n≤10000 followed by a permutation π of length n.
#
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

f = open("input.txt","r").read().split()
n = int(f[0])
pi = f[1::]

