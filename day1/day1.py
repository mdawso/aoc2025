def solve():

    print('--- Day 1 ---')

    instruction_list = []

    from pathlib import Path
    with open(Path('day1/input.txt')) as input_file:
        for line in input_file:
            instruction_list.append(line.strip())

    is_valid_zero = lambda x : x % 100 == 0

    zero_count = 0
    position = 50

    for inst in instruction_list:
        direction = inst[0]
        sign = 1 if direction == "R" else -1

        amount = inst[1:]
        position += sign * int(amount)

        if is_valid_zero(position): zero_count += 1

    print("Part 1 password:", zero_count)

    zero_count = 0
    position = 50

    for inst in instruction_list:
        direction = inst[0]
        amount = int(inst[1:])
        sign = 1 if direction == "R" else -1

        for _ in range(amount):
            position = (position + sign) % 100
            if position == 0:
                zero_count += 1


    print("Part 2 password:", zero_count)
