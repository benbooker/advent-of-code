
left = []
right = []
appearances = {}
total = 0

with open('input.txt', 'r') as file:
    for line in file:
        vals = line.split() 
        left.append(int(vals[0]))
        right.append(int(vals[1]))


for l in left:
    if not l in appearances:
        appearances[l] = right.count(l)
    total += l * appearances[l]

print(total)