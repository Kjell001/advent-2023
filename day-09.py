history_right = 0
history_left = 0

with open('input-09.txt') as file:
	for line in file:
		num = [int(s) for s in line.strip().split()]
		sum_right = 0
		sum_left = 0
		while not all(n == 0 for n in num):
			sum_right += num[-1]
			sum_left = num[0] - sum_left
			num = [num[i] - num[i-1] for i in range(1, len(num))]
		print(sum_left, sum_right)
		history_right += sum_right
		history_left -= sum_left

print(f'Part 1: {history_right}')
print(f'Part 2: {history_left}')

