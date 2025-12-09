ranges = []

with open("input.txt") as f:
    contents = f.read()
    contents = contents.split(',')
    for r in contents:
        lower, upper = r.split('-')
        ranges.append(range(int(lower),int(upper) + 1))

def is_invalid_id_p1(id : int) -> bool:
    id = str(id)
    h1, h2 = id[:len(id)//2], id[len(id)//2:]
    if h1 == h2: return True
    else: return False

sum = 0
for r in ranges:
    for v in r:
        if is_invalid_id_p1(v): sum += v

print('Part 1 sum:', sum)

def is_invalid_id_p2(id : int) -> bool:
    id = str(id)
    return id in (id + id)[1:-1]

sum = 0
for r in ranges:
    for v in r:
        if is_invalid_id_p2(v): sum += v

print('Part 2 sum:', sum)