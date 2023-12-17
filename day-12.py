from functools import cache

@cache
def process_records(records, groups, count=0):
	if not records:
		return not groups or len(groups) == 1 and count == groups[0]
	resolved = 0
	for symbol in ('#.' if records[0] == '?' else records[0]):
		if symbol == '#' and groups and count < groups[0]:
				resolved += process_records(records[1:], groups, count + 1)
		elif symbol == '.':
			if count == 0:
				resolved += process_records(records[1:], groups)
			elif groups and count == groups[0]:
				resolved += process_records(records[1:], groups[1:])
	return resolved

def count_permutations(repetitions):
	permutations = 0
	with open('input-12.txt') as file:
		for line in file:
			records, groups = line.strip().split()
			records = '?'.join([records] * repetitions)
			groups = tuple(int(s) for s in groups.split(',')) * repetitions
			permutations += process_records(records, groups)
	return permutations

print(f'Part 1: {count_permutations(1)}')
print(f'Part 2: {count_permutations(5)}')

