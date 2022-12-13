with open("ch_09", 'r') as f:
    data = f.read().splitlines()

offsets = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
movements = {(0, 2): (0, 1), (0, -2): (0, -1), (2, 0): (1, 0), (-2, 0): (-1, 0),
            (1, 2): (1, 1), (2, 1): (1, 1), (-1, 2): (-1, 1), (-2, 1): (-1, 1),
            (1, -2): (1, -1), (2, -1): (1, -1), (-1, -2): (-1, -1), (-2, -1): (-1, -1),
             (2, 2): (1, 1), (-2, 2): (-1, 1), (-2, -2): (-1, -1), (2, -2): (1, -1)}

def rope_movement(num_knots=2):
    t_visited = {(0, 0)}
    knots = [(0,0) for _ in range(num_knots)]
    for instruction in data:
        direction, distance = instruction.split()
        x, y = offsets[direction]
        for _ in range(int(distance)):
            knots[0] = (knots[0][0] + x, knots[0][1] + y)
            for i, k in enumerate(knots[1:], 1):
                diff = (knots[i-1][0] - k[0], knots[i-1][1] - k[1])
                move = movements.get(diff)
                if move:
                    knots[i] = (k[0] + move[0], k[1] + move[1])
                    if i == len(knots) - 1:
                        t_visited.add(knots[i])
    return len(t_visited)


print(rope_movement(2), rope_movement(10))