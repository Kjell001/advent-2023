import re

pattern = re.compile(r'([%&]?)(\S+) -> (.+)')

class Module:
	def __init__(self, name, type='', out=None):
		self.name = name
		self.type = type
		self.out = re.split(r', ', out) if out else []
		self.store = {}
		self.state = 0
	
	def __repr__(self):
		return f'{self.type}{self.name}'
	
	def buffer(self, source, incoming):
		#print(f'{source} -> {self}: {int(incoming)}')
		global total_low, total_high
		total_low += not incoming
		total_high += incoming
		return lambda: self.process(source, incoming)
	
	def process(self, source, incoming):
		if self.type == '&':
			self.store[source] = incoming
			outgoing = not all(self.store.values())
		elif self.type == '%':
			if incoming: return []
			self.state = self.state if incoming else not self.state
			outgoing = self.state
		else:
			outgoing = incoming
		return [m.buffer(self, outgoing) for m in self.out]

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

# Process
i, total_low, total_high = 0, 0, 0
for i in range(1000):
	queue = [modules['broadcaster'].buffer(None, 0)]
	while queue:
		queue += queue.pop(0)()

print(f'Part 1: {total_low * total_high}')

