def solve():

    print('--- Day 4 ---')

    floor = []

    from pathlib import Path
    with open(Path('day4/input.txt')) as f:
        for line in f:
            floor.append(list(line.strip()))

    rows = len(floor)
    cols = len(floor[0])

    def check_cell(r, c) -> bool:
        if 0 <= r < rows and 0 <= c < cols:
            return floor[r][c] == '@'
        return False

    def count_adjacent(r, c) -> int:
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                if check_cell(r + dr, c + dc):
                    count += 1
        return count

    count = 0
    for r in range(rows):
        for c in range(cols):
            if check_cell(r, c):
                if count_adjacent(r, c) < 4:
                    count += 1

    print('Part 1 count:', count)

    def set_cell(r,c,on):
        if 0 <= r < rows and 0 <= c < cols:
            floor[r][c] = '@' if on else '.'

    count = 0
    while True:
        subcount = 0
        for r in range(rows):
            for c in range(cols):
                if check_cell(r, c):
                    if count_adjacent(r, c) < 4:
                        set_cell(r,c,False)
                        subcount += 1
        if subcount > 0: count += subcount
        else: break

    print('Part 2 count:', count)
