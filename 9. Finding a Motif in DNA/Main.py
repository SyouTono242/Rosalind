# Given: Two DNA strings s and t (each of length at most 1 kbp).
#
# Return: All locations of t as a substring of s.

f = open("input.txt","r")
content = f.read().split()
s = content[0]
t = content[1]

list = []
for i in range(len(s)):
    if s.startswith(t, i):
        list.append(str(i+1))
print(" ".join(list))
