import re, math

pattern = re.compile(r'([%&]?)(\S+) -> (.+)')

class Module:
	def __init__(self, name, type='', out=None):
		self.name = name
		self.type = type
		self.out = re.split(r', ', out) if out else []
		self.store = {}
		self.state = 0
		self.outgoing = None
	
	def __repr__(self):
		return f'{self.type}{self.name}({len(self.out)})'
	
	def buffer(self, source, incoming):
		#print(f'{source} -> {self}: {int(incoming)}')
		global total_low, total_high
		total_low += not incoming
		total_high += incoming
		return lambda: self.process(source, incoming)
	
	def process(self, source, incoming):
		if self.type == '&':
			self.store[source] = incoming
			self.outgoing = not all(self.store.values())
		elif self.type == '%':
			if incoming: return []
			self.state = self.state if incoming else not self.state
			self.outgoing = self.state
		else:
			self.outgoing = incoming
		return [m.buffer(self, self.outgoing) for m in self.out]

# Parse
modules = {}
with open('input-20.txt') as file:
	for line in file:
		type, name, out = pattern.findall(line.strip())[0]
		modules[name] = Module(name, type, out)

for module in [*modules.values()]:
	out = []
	for other in module.out:
		modules.setdefault(other, Module(other))
		out.append(modules[other])
		modules[other].store[module] = 0
	module.out = out

# Identify groups
funnel = next(m for m in modules.values() if modules['rx'] in m.out)
nodes = [m for m in modules.values() if funnel in m.out]
periods = {}

# Process
i, total_low, total_high = 0, 0, 0
result = True
while len(periods) < len(nodes) or i < 1000:
	i += 1
	queue = [modules['broadcaster'].buffer(None, 0)]
	while queue:
		queue += queue.pop(0)()
		for m in nodes:
			if m.outgoing and m not in periods:
				periods[m] = i
	if i == 1000:
		print(f'Part 1: {total_low * total_high}')

print(f'Part 2: {math.lcm(*periods.values())}')

