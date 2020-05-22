# Given: A positive integer n≤10000 followed by a permutation π of length n.
#
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

def sub(pi, n):
    M = [None]*n
    P = [None]*n
    L = 1
    M[0] = 0

    # Binary search
    for i in range(1, n):
        lower = 0
        upper = L
        if pi[M[upper-1]] < pi[i]:
            j = upper
        else:
            while upper - lower > 1:
                mid = (upper+lower)//2
                if pi[M[mid-1]] < pi[i]:
                    lower = mid
                else:
                    upper = mid
            j = lower
        P[i] = M[j-1]
        if j == L or pi[i] < pi[M[j]]:
            M[j] = i
            L = max(L, j+1)

    result = []
    pos = M[L-1]
    for m in range(L):
        result.append(pi[pos])
        pos = P[pos]

    return result[::-1]


f = open("input.txt","r").read().split()
n = int(f[0])                   # length of the sequence
pi = [int(x) for x in f[1::]]   # the sequence

out = open("output.txt","w")
inc = sub(pi,n)
dec = sub(pi[::-1],n)[::-1]
out.write(" ".join(str(x) for x in inc)+"\n"+" ".join(str(x) for x in dec))
