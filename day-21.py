STEPS = 64

with open('input-21.txt') as file:
	map = [row + col * 1j for row, line in enumerate(file) for col, s in enumerate(line.strip()) if s in '.S']

start = map[-1] / 2
queue = {start}
dirs = (1, 1j, -1, -1j)
reach = set()
for _ in range(STEPS + 1):
	reach |= queue
	queue = {c + d for c in queue for d in dirs if c + d in map and c + d not in reach}

parity = round(start.real + start.imag) % 2
options = [c for c in reach if round(c.real + c.imag) % 2 == parity]
print(f'Part 1: {len(options)}')

