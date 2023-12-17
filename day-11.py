chart = []

with open('input-11-ex.txt') as file:
	lines = file.readlines()

empty_rows = list(range(len(lines)))
empty_cols = list(range(len(lines[0].strip())))
for row, line in enumerate(lines):
	for col, s in enumerate(line):
		if s == '#':
			if row in empty_rows: empty_rows.remove(row)
			if col in empty_cols: empty_cols.remove(col)
			chart.append((row, col))

total_1, total_2 = 0, 0
for i, coord_A in enumerate(chart):
	for j, coord_B in enumerate(chart):
		if j > i:
			row_A, row_B = sorted([coord_A[0], coord_B[0]])
			col_A, col_B = sorted([coord_A[1], coord_B[1]])
			expansion = (
				sum(1 for i in empty_rows if i in range(row_A, row_B))
				+ sum(1 for i in empty_cols if i in range(col_A, col_B))
			)
			total_1 += (row_B - row_A) + (col_B - col_A) + expansion
			total_2 += (row_B - row_A) + (col_B - col_A) + expansion * 999999

print(f'Part 1: {total_1}')
print(f'Part 1: {total_2}')

