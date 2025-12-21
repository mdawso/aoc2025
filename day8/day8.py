def solve():

    print('--- Day 8 ---')

    boxes = []
    from pathlib import Path
    with open(Path('day8/input.txt')) as f:
        for line in f:
            box = tuple(map(int, line.strip().split(',')))
            boxes.append(box)

    from math import sqrt
    def distance_between_boxes(b1, b2):
        return sqrt(
            abs(b1[0] - b2[0]) ** 2 +
            abs(b1[1] - b2[1]) ** 2 +
            abs(b1[2] - b2[2]) ** 2
        )

    pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = distance_between_boxes(boxes[i], boxes[j])
            pairs.append((dist, i, j))

    pairs.sort(key=lambda x: x[0])
    
    parent = list(range(len(boxes)))
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    limit = 1000
    for dist, i, j in pairs[:limit]:
        union(i, j)

    from collections import Counter
    circuit_roots = [find(i) for i in range(len(boxes))]
    circuit_sizes = Counter(circuit_roots)
    
    sizes = list(circuit_sizes.values())
    sizes.sort(reverse=True)
    
    result = 1
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
    elif len(sizes) > 0:
        for s in sizes:
            result *= s
    else:
        result = 0


    print(f"Part 1 result: {result}")

    parent = list(range(len(boxes)))
    num_components = len(boxes)
    
    part2_result = 0
    
    for dist, i, j in pairs:
        if union(i, j):
            num_components -= 1
            if num_components == 1:
                part2_result = boxes[i][0] * boxes[j][0]
                break
                
    print(f"Part 2 result: {part2_result}")