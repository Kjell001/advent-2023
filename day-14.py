def shift(seq, rev=False):
	return '#'.join(''.join(sorted(list(g), reverse=rev)) for g in seq.split('#'))

def transpose(map):
	return tuple(''.join(row[i] for row in map) for i in range(len(map[0])))

def cycle(map):
	for i in range(4):
		map = transpose(map)
		map = tuple(shift(seq, not i // 2 % 2) for seq in map)
	return map

def get_period(map):
	hist = {}
	for i in range(10000):
		key = map
		if key in hist:
			return hist[key], i - hist[key]
		map = cycle(map)
		hist[key] = i

def get_load(map):
	return sum(row.count('O') * (len(map) - i) for i, row in enumerate(map))

with open('input-14.txt') as file:
	ref = tuple(line.strip() for line in file)

map = transpose(ref)
map = tuple(shift(seq, True) for seq in map)
map = transpose(map)
print(f'Part 1: {get_load(map)}')

offset, period = get_period(ref)
true_cycles = (1000000000 - offset) % period + offset
map = ref
for i in range(true_cycles):
	map = cycle(map)
print(f'Part 2: {get_load(map)}')

