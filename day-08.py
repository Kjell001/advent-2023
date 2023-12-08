from math import lcm

def traverse(start, goals):
	i = 0
	node = start
	while node not in goals:
		node = map[node][dir[i % len(dir)]]
		i += 1
	return i

with open('input-08.txt') as file:
	dir = [s == 'R' for s in next(file).strip()]
	next(file)
	map = {line[:3]: (line[7:10], line[12:15]) for line in file}

starts = [node for node in map.keys() if node[2] == 'A']
goals = [node for node in map.keys() if node[2] == 'Z']

steps = [traverse(start, goals) for start in starts]

print(f'Part 1: {traverse("AAA", ["ZZZ"])}')
print(f'Part 2: {lcm(*[traverse(start, goals) for start in starts])}')

