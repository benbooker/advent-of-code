
left = []
right = []
total = 0

with open('input.txt', 'r') as file:
    for line in file:
        vals = line.split() 
        left.append(int(vals[0]))
        right.append(int(vals[1]))

left.sort()
right.sort()

for l, r in zip(left, right): 
    total += abs(l - r)

print(total)


#1 4 7 10 12 13 14 15