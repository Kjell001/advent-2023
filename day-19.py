import re
from copy import deepcopy

pat_info = re.compile(r'(.+)\{.+,(.+)\}')
pat_rules = re.compile(r'(.[<>]\d+):(\w+),')
pat_rules2 = re.compile(r'(.)([<>])(\d+):(\w+),')
pat_values = re.compile(r'\d+')

def make_func(rule):
	exp, p = rule
	return lambda: p if eval(exp) else None

flows = {}
total = 0
with open('input-19.txt') as file:
	# Read rules
	for line in file:
		if line == '\n': break
		name, fallback = pat_info.findall(line)[0]
		funcs = [make_func(rule) for rule in pat_rules.findall(line)]
		rules = [(c, s, int(v), p) for c, s, v, p in pat_rules2.findall(line)]
		flows[name] = (funcs, rules, fallback)
	# Process xmas values
	for line in file:
		x, m, a, s = [int(v) for v in pat_values.findall(line)]
		key = 'in'
		while key not in 'AR':
			funcs, _, fallback = flows[key]
			key = next((func() for func in funcs if func() is not None), None) or fallback
		total += (x + m + a + s) if key == 'A' else 0

print(f'Part 1: {total}')

# Traverse tree while updating limits per branch
base = range(1, 4001)
open = [('in', 0, {'x': {*base}, 'm': {*base}, 'a': {*base}, 's': {*base}})]
total = 0
while open:
	name, index, lim = open.pop(0)
	# Check if branch terminates
	if name == 'A':
		total += len(lim['x']) * len(lim['m']) * len(lim['a']) * len(lim['s'])
		continue
	if name == 'R': continue
	# Branch
	_, rules, fallback = flows[name]
	c, s, v, p = rules[index]
	sub = {*(range(1, v) if s == '<' else range(v + 1, 4001))}
	lim_new = deepcopy(lim)
	lim_new[c] &= sub
	open.append((p, 0, lim_new))
	lim_new = deepcopy(lim)
	lim_new[c] -= sub
	open.append((name, index + 1, lim_new) if index + 1 < len(rules) else (fallback, 0, lim_new))

print(f'Part 2: {total}')

