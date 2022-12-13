from collections import deque
import numpy as np
import plotly.offline as go_offline
import plotly.graph_objects as go


class bcolors:
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


offsets = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}


letter_map = {x: i for i, x in enumerate("SabcdefghijklmnopqrstuvwxyzE")}


def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name, "r", newline=None) as fh:
            maze = [[char for char in line.strip("\r\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except IOError as e:
        print("There is a problem with the file you have selected.", e)
        raise SystemExit


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


class Queue:
    def __init__(self, items=None):
        if items is None:
            self.items = deque()
        else:
            self.items = deque(items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]


def bfs(maze, start, goal):
    q = Queue()
    q.enqueue(start)
    discovered = {start: None}

    while q:
        pos = q.dequeue()
        if pos == goal:
            return get_path(discovered, start, goal)
        for direction in ['up', 'right', 'down', 'left']:
            i, j = offsets[direction]
            neighbour = (i + pos[0], j + pos[1])
            if is_legal_pos(maze, neighbour) and neighbour not in discovered:
                n_val = letter_map[maze[neighbour[0]][neighbour[1]]]
                pos_val = letter_map[maze[pos[0]][pos[1]]]
                if n_val <= pos_val + 1:
                    q.enqueue(neighbour)
                    discovered[neighbour] = pos
    return None


def plot_path(maze, path):
    number_maze = np.array([[letter_map[x] for x in row] for row in maze])
    fig = go.Figure(data=[go.Surface(z=number_maze)])
    fig.update_layout(
        title="Maze",
        autosize=False,
        width=1080,
        height=720,
        margin=dict(l=65, r=50, b=65, t=90),
    )
    fig.add_trace(
        go.Scatter3d(
            x=[x[1] for x in path],
            y=[x[0] for x in path],
            z=[number_maze[x[0], x[1]] for x in path],
            mode="lines",
            line=dict(color="red", width=5),
        )
    )
    go_offline.plot(fig, filename="maze.html")


    # new_maze = [row[:] for row in maze]
    # for coord in path:
    #     if coord == path[0]:
    #         new_maze[coord[0]][coord[1]] = bcolors.OKBLUE + "S" + bcolors.ENDC
    #     elif coord == path[-1]:
    #         new_maze[coord[0]][coord[1]] = bcolors.FAIL + "E" + bcolors.ENDC
    #     else:
    #         new_maze[coord[0]][coord[1]] = bcolors.OKGREEN + new_maze[coord[0]][coord[1]] + bcolors.ENDC
    # for row in new_maze:
    #     print(" ".join(row))


def find_edges(maze):
    edges = []
    for i, row in enumerate(maze):
        if i == 0 or i == len(maze) - 1:
            for j, col in enumerate(row):
                if col == "a":
                    edges.append((i, j))
        else:
            if row[0] == "a":
                edges.append((i, 0))
            if row[-1] == "a":
                edges.append((i, len(row) - 1))
    return edges


def main(maze, start=None, goal=None, plot=False):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == "S" and start is None:
                start = (i, j)
            elif col == "E" and goal is None:
                goal = (i, j)
    if not start or not goal:
        print("No start or goal found.")
        raise SystemExit

    path = bfs(maze, start, goal)
    if path:
        if plot:
            plot_path(maze, path)
        return len(path) - 1
    else:
        return None



if __name__ == "__main__":
    maze = read_maze("ch_12")
    print(main(maze, plot=True))

    edges = find_edges(maze)
    least_steps = 0
    for edge in edges:
        steps = main(maze, start=edge)
        if steps:
            if least_steps == 0 or steps < least_steps:
                least_steps = steps
    print(least_steps)


