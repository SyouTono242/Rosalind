# Given: A DNA string of length at most 1 kbp in FASTA format.
#
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may
#         return these pairs in any order.

# Compliment dictionary
dict = {
    "A":"T", "T":"A",
    'G':"C", "C":"G",
    "#":"#"
}

# Find the reverse palindrome using an altered version of Manacher's algorithm
# Modify the string
DNA = "".join(open("input.txt","r").read().split()[1::])
newDNA = "#"+"#".join(list(DNA))+"#"

RL=[0]*len(newDNA)  # RL stores the length of palindrome
MaxRight = 0        # MaxRight stores the farthest character ever visited
pos = 0             # pos stores the position of the symmetric center
for i in range(len(newDNA)):
    if i<MaxRight:
        RL[i]=min(RL[2*pos-i], MaxRight-i)
    # try to expand the reverse palindrome zone until it's no longer symmetric or either end of the string is met
    while i-RL[i]>=0 and i+RL[i]<len(newDNA) and newDNA[i-RL[i]]==dict[newDNA[i+RL[i]]]:
        RL[i]+=1
    # Update MaxRight and pos when current MaxRight is visited
    if RL[i]+i-1>MaxRight:
        MaxRight=RL[i]+i-1
        pos=i
for j in range(len(RL)):
    RL[j] = RL[j]-1
# Remove RL that's corresponding to nucleotides
RL = RL[0::2]

for n in range(len(RL)):
    if 4<=RL[n]<=12:
        print(int(n-RL[n]/2+1),RL[n])
        # Print reverse palindromes with the same symmetric center
        if RL[n]>4:
            for m in range(0,int(RL[n]/2-2)):
                print(int(n-RL[n]/2+2+m),RL[n]-2*(m+1))
