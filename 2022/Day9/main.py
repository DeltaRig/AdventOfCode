from pathlib import Path


file = 'input.txt'
lines = Path(file).read_text().splitlines()

# Initialize head and tail positions
head = (0, 0)
tail = (0, 0)
visited_positions = {(0, 0)}

for instruction in lines:
    direction, steps = parse_instruction(instruction)
    for _ in range(steps):
        move_head(direction)
        move_tail()  # Adjust tail to stay close to head
        visited_positions.add(tail_position)

print(len(visited_positions))
