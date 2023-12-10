import re

dirs = {
	'-': [0, 2], '|': [1, 3], 'J': [1, 2], '7': [2, 3],
	'F': [3, 0], 'L': [0, 1], 'S': [0, 1, 2, 3]
}

offsets = [(0, 1), (-1, 0), (0, -1), (1, 0)]

with open('input-10.txt') as file:
	grid = [line.strip() for line in file]
	n_rows = len(grid)
	n_cols = len(grid[0])

# Traverse loop while tracking length and perimeter
row, col = next((i, row.find('S')) for i, row in enumerate(grid) if 'S' in row)
sym = 'S'
dir_from = None
length = 0
dir_S = None
perimeter = {}
while True:
	perimeter.setdefault(row, []).append(col)
	for dir in dirs[sym]:
		if dir != dir_from:
			row_new = row + offsets[dir][0]
			col_new = col + offsets[dir][1]
			if row_new in range(n_rows) and col_new in range(n_cols):
				sym = grid[row_new][col_new]
				dir_new = (dir + 2) % 4
				if dir_new in dirs[sym]:
					dir_S = dir if dir_S is None else dir_S
					row, col, dir_from = row_new, col_new, dir_new
					length += 1
					break
	if sym == 'S':
		break

# Replace S with appropriate pipe
sub_S = next(sym for sym, dir in dirs.items() if dir_S in dir and dir_new in dir)
# Count area per line by counting perimeter crossings
inside = 0
for row in range(n_rows):
	line = grid[row].replace('S', sub_S)
	line = ''.join(s if i in perimeter.get(row, []) else '.' for i, s in enumerate(line))
	segments = re.split(r'\||F-*J|L-*7', line)
	inside += sum(seg.count('.') for seg in segments[1::2])

print(f'Part 1: {round(length / 2)}')
print(f'Part 2: {inside}')

