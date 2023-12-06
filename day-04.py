score_total = 0
matches = {}
count = 0
with open('input-04.txt', 'r') as file:
	for index, line in enumerate(file):
		winning, check = [[int(n) for n in s.split()] for s in line[9:].strip().split('|')]
		match = sum(i in winning for i in check)
		score_total += 2 ** (match - 1) if match else 0
		# Part 2
		for i in range(match):
			matches[index + i + 1] = matches.get(index + i + 1, 0) + 1 + matches.get(index, 0)
		count += 1 + matches.get(index, 0)
		#print(match, matches.get(index, 0), count)
		

print(f'Part 1: {score_total}')
print(f'Part 2: {count}')

