test = {'red': 12, 'green': 13, 'blue': 14}
id_sum = 0
power_sum = 0

with open('input-02.txt', 'r') as file:
	for i, line in enumerate(file):
		legal = True
		col_max = {'red': 0, 'green': 0, 'blue': 0}
		_, specs = line.split(': ')
		for spec in specs.split('; '):
			pairs = [col.split() for col in spec.split(', ')]
			for num, col in pairs:
				if int(num) > test[col]:
					legal = False
				col_max[col] = max(int(num), col_max[col])
		id_sum += (i + 1) if legal else 0
		power = 1
		for lim in col_max.values():
			power *= lim
		power_sum += power

print(f'Part 1: {id_sum}')
print(f'Part 2: {power_sum}')

