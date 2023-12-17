def str_diff(a, b):
	return sum(sa != sb for sa, sb in zip(a, b))

def analyse(pattern, smudge):
	for i, (A, B) in enumerate(zip(pattern[:-1], pattern[1:])):
		diff = str_diff(A, B)
		if diff in (0, smudge):
			total = diff
			test = min(i + 1, len(pattern) - i - 1)
			sub_A = pattern[i-test+1:i]
			sub_B = pattern[i+2:i+1+test]
			sub_B.reverse()
			for a, b in zip(sub_A, sub_B):
				total += str_diff(a, b)
				if total > smudge:
					break
			else:
				if total == smudge:
					return i

def process(pattern, smudge):
	axis = analyse(pattern, smudge)
	if axis is None:
		pattern = [''.join(row[i] for row in pattern) for i in range(len(pattern[0]))]
		axis = analyse(pattern, smudge)
		return axis + 1
	else:
		return 100 * (axis + 1)

def scan(smudge):
	pattern = []
	note = 0
	with open('input-13.txt') as file:
		for line in file:
			if line == '\n':
				note += process(pattern, smudge)
				pattern = []
			else:
				pattern.append(line.strip())
		note += process(pattern, smudge)
	return note

print(f'Part 1: {scan(False)}')
print(f'Part 2: {scan(True)}')

