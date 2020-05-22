f = open("input.txt","r").read().split()
n = int(f[0])
pi = [int(x) for x in f[1::]]

def lengthOfLIS(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

print(lengthOfLIS(pi))
