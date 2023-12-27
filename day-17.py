from heapq import heappush, heappop

# Store coordinates as complex numbers
with open('input-17.txt') as file:
	map = {row + col * 1j: int(s) for row, line in enumerate(file) for col, s in enumerate(line.strip())}

def find_path(smin, smax):
	start, finish = 0, list(map)[-1]
	open = [(0, 0, 1, start), (0, 0, 1j, start)]
	closed = set()
	num = 0
	while open:
		cost, _, dir, coord = heappop(open)
		if coord == finish: return cost
		# Identical (dir, coord) found further down would be less efficient
		if (dir, coord) in closed: continue
		closed.add((dir, coord))
		# Explore both left and right directions
		for dir_new in dir / 1j, dir * 1j:
			# Explore straight stretches following the turns
			for s in range(smin, smax + 1):
				coord_new = coord + dir_new * s
				if coord_new in map:
					cost_new = cost + sum(map[coord + dir_new * (i+1)] for i in range(s))
					# Track num to give priority to oldest option if same cost
					heappush(open, (cost_new, num := num + 1, dir_new, coord_new))

print(f'Part 1: {find_path(1, 3)}')
print(f'Part 2: {find_path(4, 10)}')

