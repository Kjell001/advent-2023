import re

class Sym:
	def __init__(self, m):
		self.type = m[0]
		self.pos = m.start()

class Num:
	def __init__(self, m):
		self.value = int(m[0])
		self.range = range(m.start() - 1, m.end() + 1)
		self.counted = False
	
	def count(self):
		val = self.value if not self.counted else 0
		self.counted = True
		return val

symbols = []
numbers = []

pat_sym = re.compile(r'[^\.\d]')
pat_num = re.compile(r'\d+')

with open('input-03.txt', 'r') as file:
	for line in file:
		symbols.append([Sym(m) for m in pat_sym.finditer(line.strip())])
		numbers.append([Num(m) for m in pat_num.finditer(line.strip())])

parts = 0
gears = 0
for i, srow in enumerate(symbols):
	for symbol in srow:
		gear_count = 0
		ratio = 1
		for nrow in numbers[(i-1):(i+2)]:
			for number in nrow:
				if symbol.pos in number.range:
					parts += number.count()
					if symbol.type == '*':
						ratio *= 0 if gear_count > 2 else number.value
						gear_count += 1
		gears += ratio if gear_count == 2 else 0

print(f'Part 1: {parts}')
print(f'Part 2: {gears}')

