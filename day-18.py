import re

pattern = re.compile(r'(.) (\d+) \(#(.+)(\)\)')
dirs = {'R': 1, 'D': 1j, 'L': -1, 'U': -1j}

with open('input-18.txt') as file:
	plan = [
		(dirs[d1], int(s1), [*dirs.values()][int(d2)], int(s2, 16))
		for d1, s1, s2, d2 in [pattern.findall(line)[0] for line in file]
	]

def get_area(plan):
	area, perimeter, a = 0, 0, 0
	for dir, steps in plan:
		b = a + steps * dir
		area += (b - a).real * a.imag # Shoelace formula
		perimeter += abs(b - a)
		a = b
	return int(abs(area) + perimeter / 2 + 1) # Account for half perimeter an corners

print(f'Part 1: {get_area(((d, s) for d, s, _, _ in plan))}')
print(f'Part 2: {get_area(((d, s) for _, _, d, s in plan))}')

