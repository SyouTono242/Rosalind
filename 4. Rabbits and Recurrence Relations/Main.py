# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
#         generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1
#         pair).

n = 36      # The number of months
k = 2       # The number of rabbits produced by each reproduction

Bcount = 0  # Count of big rabbits
Scount = 1  # Count of small rabbits

for time in range(1, n):
    newBcount = Bcount + Scount
    newScount = Bcount*k
    Bcount = newBcount
    Scount = newScount

print(Bcount+Scount)
