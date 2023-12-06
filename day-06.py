from math import sqrt, ceil
from re import sub

with open('input-06.txt', 'r') as file:
	line = file.readline()
	times1 = [int(s) for s in line.split(':')[1].split()]
	times2 = [int(sub(r'[^\d]', '', line))]
	line = file.readline()
	dists1 = [int(s) for s in line.split(':')[1].split()]
	dists2 = [int(sub(r'[^\d]', '', line))]

def calculate(times, dists):
	prod = 1
	for time, dist in zip(times, dists):
		D = sqrt(time ** 2 - 4 * dist)
		x1 = (time - D) / 2
		x2 = (time + D) / 2
		prod *= ceil(x2) - ceil(x1 + 1e-6)
	return prod

print(f'Part 1: {calculate(times1, dists1)}')
print(f'Part 2: {calculate(times2, dists2)}')

