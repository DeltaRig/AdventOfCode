# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12
# Daniela Rigoli at Nov 2026
from collections import deque


def findStart(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                print(f"Start found at: {i}, {j}")
                return (i, j)
    print("Start not found")
    return None

def bfs(lines, start_i, start_j):
    rows = len(lines)
    cols = len(lines[0].strip())
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_i, start_j, 0)])  # (i, j, steps)
    visited[start_i][start_j] = True

    while queue:
        i, j, steps = queue.popleft()

        if lines[i][j] == "E":
            return steps

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            # Check bounds and if the cell is not visited
            if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                # Check if the move is valid based on the height difference
                current_height = ord(lines[i][j]) if lines[i][j] not in "SE" else (ord('a') if lines[i][j] == 'S' else ord('z'))
                next_height = ord(lines[ni][nj]) if lines[ni][nj] not in "SE" else (ord('a') if lines[ni][nj] == 'S' else ord('z'))
                if next_height - current_height <= 1:
                    if lines[ni][nj] == 'E':# verify if we can end
                        return steps + 1
                    queue.append((ni, nj, steps + 1))
                    visited[ni][nj] = True

    return -1  # If the end is not reachable


# read input.txt

with open("input.txt", "r") as f:
    lines = f.readlines()

i, j = findStart(lines)

# Breadth-First Search
steps = bfs(lines, i, j)
print(f"Steps to reach the end: {steps}")