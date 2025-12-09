ranges = []
ranges_tuples = []
available = []

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if '-' in line:
            lower, upper = line.split('-')
            ranges_tuples.append((int(lower),int(upper)))
            ranges.append(range(int(lower),int(upper) + 1))
        elif line == '':
            continue
        else:
            available.append(int(line))

fresh = set()
for r in ranges:
    for id in available:
        if id in r: fresh.add(id)

print('Part 1 count:', len(fresh))

ranges_tuples.sort(key=lambda x: x[0])
merged = []
current_lower, current_upper = ranges_tuples[0]
for lower, upper in ranges_tuples[1:]:
    if lower <= current_upper + 1: # Overlap
        current_upper = max(current_upper, upper)
    else: # No overlap
        merged.append((current_lower, current_upper))
        current_lower, current_upper = lower, upper

merged.append((current_lower, current_upper))
count = sum(upper - lower + 1 for lower, upper in merged)

print('Part 2 count:', count)