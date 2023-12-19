reflect = {
	'/':  lambda x: [(-x[1], -x[0])],
	'\\': lambda x: [(x[1], x[0])],
	'.':  lambda x: [x],
	'-':  lambda x: [(0, -1), (0, 1)] if x[0] else [x],
	'|':  lambda x: [(-1, 0), (1, 0)] if x[1] else [x],
}

def go(track, queue):
	dir, pos = queue.pop(0)
	step = (dir, pos)
	# Track
	if step in track:
		return
	track.add(step)
	# Determine next
	for new_dir in reflect[map[pos]](dir):
		new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
		if new_pos in map:
			key = (new_dir, new_pos)
			queue.append(key)

with open('input-16.txt') as file:
	lines = file.readlines()
	dim = (len(lines), len(lines[0].strip()))
	map = {(row, col): s for row, line in enumerate(lines) for col, s in enumerate(line.strip())}

def traverse(start):
	track = set()
	queue = [start]
	while queue:
		go(track, queue)
	return len(set(t[1] for t in track))

starts = (
	  [(( 0,  1), (       row,          0)) for row in range(dim[0])]
	+ [(( 0, -1), (       row, dim[1] - 1)) for row in range(dim[0])]
	+ [(( 1,  0), (         0,        col)) for col in range(dim[1])]
	+ [((-1,  0), (dim[0] - 1,        col)) for col in range(dim[1])]
)

print(f'Part 1: {traverse(((0, 1), (0, 0)))}')
print(f'Part 2: {max(traverse(start) for start in starts)}')

