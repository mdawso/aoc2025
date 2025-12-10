rows = []

with open('input.txt') as f:
    for line in f:
        rows.append(list(line.strip()))

count = 0
for i in range(len(rows) - 1):
    top = rows[i]
    bottom = rows[i+1]
    for j in range(len(top) -1):
        top_char = top[j]
        bottom_char = bottom[j]
        if top_char == 'S' and bottom_char == '.':
            bottom[j] = '|'
        if top_char == '|' and bottom_char == '^':
            bottom[j-1] = '|'
            bottom[j+1] = '|'
            count += 1
        if top_char == '|' and bottom_char == '.':
            bottom[j] = '|'

print('Part 1 count:', count)

# for row in rows:
#     s = ''
#     for c in row:
#         s += str(c)
#     print(s)

