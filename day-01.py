import re

map = {
	'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
	'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
	'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

pat = [
	re.compile(f'(?=(\\d))'),
	re.compile(f'(?=({"|".join(map.keys())}))')
]
num = [[], []]
with open('input-01.txt', 'r') as file:
	for line in file:
		for i in [0, 1]:
			m = list(pat[i].finditer(line))
			num[i].append(map[m[0][1]] * 10 + map[m[-1][1]])
		
print(f'Part 1: {sum(num[0])}')
print(f'Part 2: {sum(num[1])}')

