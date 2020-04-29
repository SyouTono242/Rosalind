def cons(strings):
    from collections import Counter
    counters = map(Counter, zip(*strings))
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
    profile_matrix = "\n".join(b + ": " + \
        " ".join(str(c[b]) for c in counters) for b in "ACGT")
    return consensus + "\n" + profile_matrix

f = open("input.txt","r")
lines = f.read().split(">")
lines.remove(lines[0])
newLines = []
for string in lines:
    string = string.lstrip("Rosalind_")
    string = "".join([i for i in string if not (i.isdigit())])
    newLines.append(string.replace("\n",""))
print(cons(newLines))
