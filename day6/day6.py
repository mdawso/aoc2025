lines = [line.rstrip("\n") for line in open("input.txt")]

width = max(len(line) for line in lines)
normalized = [line.ljust(width) for line in lines]

problems = []
current_cols = []

for col in range(width):
    column_chars = [row[col] for row in normalized]
    if all(ch == " " for ch in column_chars):
        if current_cols:
            problems.append(current_cols)
            current_cols = []
    else:
        current_cols.append(column_chars)

# last problem
if current_cols:
    problems.append(current_cols)

totals = []

for prob in problems:
    rows = ["".join(col[i] for col in prob) for i in range(len(lines))]
    rows = [r.strip() for r in rows if r.strip()]

    *nums, op = rows

    nums = list(map(int, nums))

    match op:
        case '+': total = sum(nums)
        case '*':
            total = 1
            for n in nums:
                total *= n

    totals.append(total)

print("Part 1 total:", sum(totals))

totals_p2 = []

for prob in problems:
    rows = ["".join(col[i] for col in prob) for i in range(len(lines))]
    op_row = rows[-1]
    op = op_row.strip()[-1] 
    num_rows = rows[:-1]
    num_cols = list(zip(*num_rows))
    num_cols_rtl = reversed(num_cols)

    nums = []
    for col in num_cols_rtl:
        num_str = "".join(col).strip()
        if num_str:
            nums.append(int(num_str))

    match op:
        case '+': total = sum(nums)
        case '*':
            total = 1
            for n in nums:
                total *= n
    
    totals_p2.append(total)

print("Part 2 total:", sum(totals_p2))