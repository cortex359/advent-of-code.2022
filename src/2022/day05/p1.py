with open("input") as file:
	data = [line.removesuffix("\n") for line in file]

crates = 0
for line in data:
	if line != "":
		crates += 1
	else:
		break

no_of_crates = int(data[crates-1].split()[-1])

stack: list[list[str]] = []

for c in range(0, no_of_crates):
	elements = []
	for line in data[:crates-1]:
		if len(line) >= c*4+1:
			if line[(c*4)+1] != " ":
				elements.append(line[(c*4)+1])
	elements.reverse()
	stack.append(elements)

for line in data[crates+1:]:
	size = int(line.split()[1])
	src = int(line.split()[3]) - 1
	dest = int(line.split()[5]) - 1

	for s in range(size):
		stack[dest].append(stack[src][-1])
		stack[src].pop()

output = ""
for s in stack:
	output += s[-1]

print(output)