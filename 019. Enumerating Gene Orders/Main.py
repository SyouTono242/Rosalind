# Given: A positive integer n≤7.
#
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

def to_string(list):
    return " ".join(list)

def permute(list, start, end):
    if start == end:
        print(to_string(list))
    else:
        for i in range(start, end+1):
            list[start], list[i] = list[i], list[start]
            permute(list, start+1, end)
            list[start], list[i] = list[i], list[start]

n = 6
i = n
intList = []
counter = 1
while i > 0:
    intList.append(str(i))
    counter = counter * i
    i -= 1

print(counter)
permute(intList, 0, len(intList)-1)
