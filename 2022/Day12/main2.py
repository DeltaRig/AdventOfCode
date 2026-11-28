# Day 12: Hill Climbing Algorithm part 2
# https://adventofcode.com/2022/day/12
# Daniela Rigoli at Nov 2026
from collections import deque

def findAllA(lines):
    a_positions = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "a":
                a_positions.append((i, j))
    return a_positions

def bfs(lines, positions):
    rows = len(lines)
    cols = len(lines[0].strip())
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(i, j, 0) for i, j in positions])  # (i, j, steps)
    for i, j in positions:
        visited[i][j] = True

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

positions = findAllA(lines)

# Breadth-First Search
steps = bfs(lines, positions)
print(f"Steps to reach the end: {steps}")