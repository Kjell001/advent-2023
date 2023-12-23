import re

pattern = re.compile(r'(.) (\d+) \(#(.+)(.)\)')
dirs = {'R': 1, 'D': 1j, 'L': -1, 'U': -1j}
with open('input-18-ex.txt') as file:
	plan = [(dirs[d1], int(s1), [*dirs.values()][int(d2)], int(s2, 16)) for d1, s1, s2, d2 in [pattern.findall(line)[0] for line in file]]

def get_area(plan):
	# Perimeter
	start = 0
	neg, mid, pos = set(), set(), set()
	for dir, steps in plan:
		seg = [start + dir * i for i in range(steps + 1)]
		neg |= {coord + dir * -1j for coord in seg}
		mid |= {coord             for coord in seg}
		pos |= {coord + dir *  1j for coord in seg}
		start = seg[-1]
	# Fill
	open = pos if len(pos := pos - mid) < len(neg := neg - mid) else neg
	area = set()
	while open:
		coord = open.pop()
		if coord not in mid and coord not in area:
			area.add(coord)
			open |= {coord + dir for dir in dirs.values()}
	return len(mid | area)

print(f'Part 1: {get_area(((d, s) for d, s, _, _ in plan))}')
#print(f'Part 2: {get_area(((d, s) for _, _, d, s in plan))}')

