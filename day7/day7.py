def solve():

    print('--- Day 7 ---')

    rows = []

    from pathlib import Path
    with open(Path('day7/input.txt')) as f:
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

    rows = []

    from pathlib import Path
    with open(Path('day7/input.txt')) as f:
        for line in f:
            rows.append(list(line.strip()))

    height = len(rows)
    width = len(rows[0])

    timeline_counts = [[0 for _ in range(width)] for _ in range(height)]

    for r in range(height):
        for c in range(width):
            if rows[r][c] == 'S':
                timeline_counts[r][c] = 1

    for r in range(height - 1):
        for c in range(width):
            current_count = timeline_counts[r][c]

            if current_count == 0:
                continue

            char_below = rows[r+1][c]

            if char_below == '^':
                if c > 0:
                    timeline_counts[r+1][c-1] += current_count
                if c < width - 1:
                    timeline_counts[r+1][c+1] += current_count
            else:
                timeline_counts[r+1][c] += current_count

    total_timelines = sum(timeline_counts[-1])

    print('Part 2 count:', total_timelines)
