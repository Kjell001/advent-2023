import re

def hash(phrase):
	value = 0
	for s in phrase:
		value = (value + ord(s)) * 17 % 256
	return value

with open('input-15.txt') as file:
	phrases = next(file).strip().split(',')

template = re.compile(r'([a-z]+)([-=])(\d)?')
boxes = {}
for phrase in phrases:
	label, op, focal = template.findall(phrase)[0]
	box = boxes.setdefault(hash(label), {})
	if op == '=':
		box[label] = int(focal)
	elif label in box:
		del box[label]
power = sum(
	(i + 1) * (j + 1) * focal
		for i, box in boxes.items()
		for j,(label, focal) in enumerate(box.items())
	)

print(f'Part 1: {sum(hash(phrase) for phrase in phrases)}')
print(f'Part 2: {power}')

