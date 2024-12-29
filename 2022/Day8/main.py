# Daniela Rigoli Dezember 28 2024
# https://adventofcode.com/2022/day/8
from pathlib import Path

# Part 1
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

def scenicScore(lines, l, c):
    tree_height = lines[l][c]

    # Check upwards
    temp = 0
    for ll in range(l - 1, -1, -1):
        temp += 1
        if lines[ll][c] >= tree_height:
            break
    score = temp

    # Check downwards
    temp = 0
    for ll in range(l + 1, len(lines)):
        temp += 1
        if lines[ll][c] >= tree_height:
            break
    score *= temp

    # Check left
    temp = 0
    for cc in range(c - 1, -1, -1):
        temp += 1
        if lines[l][cc] >= tree_height:
            break
    score *= temp

    # Check right
    temp = 0
    for cc in range(c + 1, len(lines[0])):
        temp += 1
        if lines[l][cc] >= tree_height:
            break
    score *= temp

    return score

## interprestação de que se uma arvore maior aparece não se enxerga o que tem atras
def scenicScore2(lines, l, c):
    # Check upwards
    temp = 0
    for ll in range(l - 1, -1, -1):
        if lines[ll][c] >= lines[ll+1][c]:
            temp+=1
            break
        else: temp+=1
    score = temp

    temp = 0
    # Check downwards
    for ll in range(l + 1, len(lines)):
        if lines[ll][c] >= lines[ll-1][c]:
            temp+=1
            break
        else: temp+=1
    score = score * temp

    temp = 0
    # Check left
    for cc in range(c - 1, -1, -1):
        if lines[l][cc] >= lines[l][cc+1]:
            temp+=1
            break
        else: temp+=1
    score = score * temp

    temp = 0
    # Check right
    for cc in range(c + 1, len(lines[0])):
        if lines[l][cc] >= lines[l][cc-1]:
            temp+=1
            break
        else: temp+=1

    score = score * temp
    return score

def treeTop(file):
    lines = Path(file).read_text().splitlines()
    count = 0
    
    for c in range(1, len(lines[0])-1):
        for l in range(1, len(lines)-1):
            # print(l, " ", c, " ", lines[l][c]," ", checkVisible(lines, l, c))
            if(checkVisible(lines, l, c)):
                count+=1
    # sum the edges:
    count += (len(lines[0])-1 + len(lines)-1)*2
    return count

def treeTopHighScore(file):
    lines = Path(file).read_text().splitlines()
# part 2
#    print("1 2: ", scenicScore(lines, 1,2))
#    print("3 2 ", scenicScore(lines, 3,2))
    highest = 0
    for c in range(len(lines[0])):
        for l in range(len(lines)):
            temp = scenicScore(lines, l, c)
            if(temp > highest):
                print(temp)
                highest = temp
    return highest

    

file = 'input.txt'
result = treeTop(file)
print("Part 1:", result)
result = treeTopHighScore(file)
print("Part 2:", result)
