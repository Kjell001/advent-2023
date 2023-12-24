import re

pat_info = re.compile(r'(.+)\{.+,(.+)\}')
pat_rules = re.compile(r'(.[<>]\d+):(\w+),')
pat_values = re.compile(r'\d+')

def make_func(rule):
	exp, p = rule
	return lambda: p if eval(exp) else None

flows = {}
total = 0
with open('input-19.txt') as file:
	for line in file:
		if line == '\n': break
		name, fallback = pat_info.findall(line)[0]
		rules = [make_func(rule) for rule in pat_rules.findall(line)]
		flows[name] = (rules, fallback, line.strip())
	for line in file:
		x, m, a, s = [int(v) for v in pat_values.findall(line)]
		key = 'in'
		while key not in 'AR':
			funcs, fallback, og = flows[key]
			key = next((func() for func in funcs if func() is not None), None) or fallback
		total += (x + m + a + s) if key == 'A' else 0

print(f'Part 1: {total}')

