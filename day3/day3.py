def solve():

    print('--- Day 3 ---')

    banks = []

    from pathlib import Path
    with open(Path('day3/input.txt')) as f:
        for line in f:
            banks.append(line.strip())

    sum = 0
    for b in banks:
        bank_max = 0
        for i in range(len(b) - 1):
            for j in range(i + 1, len(b)):
                subsum = int(b[i] + b[j])
                if subsum > bank_max:
                    bank_max = subsum
        sum += bank_max

    print("Part 1 sum:", sum)

    def max_subsequence_of_length(s, k):
        stack = []
        to_pick = k
        to_drop = len(s) - k
        for digit in s:
            while stack and digit > stack[-1] and to_drop > 0:
                stack.pop()
                to_drop -= 1
            stack.append(digit)
        return ''.join(stack[:k])

    sum = 0
    for b in banks:
        best = int(max_subsequence_of_length(b, 12))
        sum += best

    print("Part 2 sum:", sum)
