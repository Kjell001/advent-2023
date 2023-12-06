def transform(seed_ranges):
	new_ranges = []
	for s in seed_ranges:
		for map in maps:
			r = map['range']
			# Test for overlap between seed range and map range
			body = range(max(s.start, r.start), min(s.stop, r.stop))
			if body:
				d = map['offset']
				new_ranges.append(range(body.start + d, body.stop + d))
				# Add left-over head and tail to current iteration
				if s.start < r.start:
					seed_ranges.append(range(s.start, r.start))
				if r.stop < s.stop:
					seed_ranges.append(range(r.stop, s.stop))
				break
		else:
			new_ranges.append(s)
	return new_ranges
			
with open('input-05.txt', 'r') as file:
	# Setup
	seeds = [int(s) for s in next(file)[6:].strip().split()]
	seed_ranges1 = [range(s, s + 1) for s in seeds]
	seed_ranges2 = [
		range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)
	]
	maps = []
	# Iterate
	for line in file:
		if not line.strip():
			# Transform
			seed_ranges1 = transform(seed_ranges1)
			seed_ranges2 = transform(seed_ranges2)
			# Reset and skip
			maps = []
			next(file)
		else:
			# Parse
			spec = [int(s) for s in line.strip().split()]
			maps.append({
				'range': range(spec[1], spec[1] + spec[2]),
				'offset': spec[0] - spec[1]
			})
	# Final transform
	seed_ranges1 = transform(seed_ranges1)
	seed_ranges2 = transform(seed_ranges2)

print(f'Part 1: {min(s.start for s in seed_ranges1)}')
print(f'Part 2: {min(s.start for s in seed_ranges2)}')

