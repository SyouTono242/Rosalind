# Given: Positive integers n≤100 and m≤20.
#
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

n = 86          # Total month
m = 19          # Rabbit dies after m months
gen = [1,1]   # List that trace the number of new born rabbits in the past m months

def fib(i,j):
    count = 2           # Months passes, initialized to be 2
    while count<i:
        if count < j:   # No rabbit died yet
            gen.append(gen[-2]+gen[-1])
        elif count == j or count == j+1:    # Rabbits are still wearing black
            gen.append((gen[-2]+gen[-1])-1)
        else:            # Rabbits have learnt to respect death
            gen.append((gen[-2]+gen[-1]) - (gen[-(j+1)]))
        count += 1
    return gen[-1]

print(fib(n,m))

