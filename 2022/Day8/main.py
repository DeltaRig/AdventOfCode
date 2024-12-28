# Daniela Rigoli Dezember 28 2024
# https://adventofcode.com/2022/day/8
from pathlib import Path
# check if is visible
# considering that it will not receive edges as it will be always visible then don't need to check
def checkVisible(lines, l, c):
    # Check upwards
    for ll in range(l - 1, -1, -1):
        if lines[ll][c] >= lines[l][c]:
            break
    else:
        return True  # Visible upwards
    # Check downwards
    for ll in range(l + 1, len(lines)):
        if lines[ll][c] >= lines[l][c]:
            break
    else:
        return True  # Visible downwards
    # Check left
    for cc in range(c - 1, -1, -1):
        if lines[l][cc] >= lines[l][c]:
            break
    else:
        return True  # Visible to the left
    # Check right
    for cc in range(c + 1, len(lines[0])):
        if lines[l][cc] >= lines[l][c]:
            break
    else:
        return True  # Visible to the right
    return False  # Not visible from any direction



def treeTop(file):
    lines = Path(file).read_text().splitlines()
    count = 0
    print(lines)
    for c in range(1, len(lines[0])-1):
        for l in range(1, len(lines)-1):
            print(l, " ", c, " ", lines[l][c]," ", checkVisible(lines, l, c))
            if(checkVisible(lines, l, c)):
                count+=1
    print(count)
    # sum the edges:
    count += (len(lines[0])-1 + len(lines)-1)*2
    

    
    return count

file = 'input.txt'
result = treeTop(file)
print("Part 1:", result)
