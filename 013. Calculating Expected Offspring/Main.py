# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of
#        couples in a population possessing each genotype pairing for a given factor. In order, the six given integers
#        represent the number of couples having the following genotypes:
#        1. AA-AA
#        2. AA-Aa
#        3. AA-aa
#        4. Aa-Aa
#        5. Aa-aa
#        6. aa-aa

# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the
#         assumption that every couple has exactly two offspring.

couple = "16081 17386 18446 16715 16384 17867".split()
couple = [int(i) for i in couple]
chance = [2,2,2,1.5,1,0]
offspring = 0

for i in range(0,6):
    offspring += couple[i]*chance[i]
print(offspring)
