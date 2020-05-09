# Faster (<0.1s) solution using Binary search on the length of the longest common substring.
# Time complexity: O(log(len)*len*len*k).

# Check if a substring is in all DNA sequences
def substr_in_all(arr, part):
  for dna in arr:
    if part not in dna:
      return False
  return True

# Find the common substrings
def common_substr(arr, l):
  first = arr[0]
  for i in range(len(first)-l+1):
    part = first[i:i+l]
    if substr_in_all(arr, part):
      return part
  return ""

# TODO: Find the longest common substring using Binary search
def longest_common_substr(arr):
  l = 0; r = len(arr[0])

  while l+1<r:
    mid = (l+r) // 2
    if common_substr(arr, mid)!="":
      l=mid
    else:
      r=mid

  return common_substr(arr, l)


def main():
    f = open("input.txt","r")
    DNAlist = []
    currDNA = ""
    for line in f:
        if line[0] == ">":
            DNAlist.append(currDNA)
            currDNA = ""
        else:
            currDNA += line.strip()
    DNAlist.append(currDNA)
    DNAlist.remove("")
    print(longest_common_substr(DNAlist))

main()
