# /**
#  * https://adventofcode.com/2023/day/3
#  * 
#  * @author (Daniela Pereira Rigoli)
#  * @version (03/12/2023)
#  */
# Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

input = [
    "467A.114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]
input = list(open("challenge3.txt", "r"))

def is_symbol(c):
    return (c != '.') and (not c.isdigit())


def is_oob(x, y, grid): #oob = out of bounds
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    return (x < 0) or (x > max_x) or (y < 0) or (y > max_y)


def has_adjacent_symbol(num_coords, num):
    coordL = num_coords[1]
    coordC = num_coords[0]
    coordCStart = coordC
    leng = len(str(num))
    coordCEnd = coordC + leng-1
    if(coordC > 0):
        coordCStart = coordC-1
        if(is_symbol(input[coordL][coordCStart])):
            return True
    
    if(coordC+ leng < len(input[0])): # checking if didn't pass the line len
        coordCEnd = coordC + leng
        if(is_symbol(input[coordL][coordCEnd])):
            return True
        
    if(coordL > 0):
        for c in range(coordCStart, coordCEnd+1):
            if(is_symbol(input[coordL-1][c])):
                return True
            
    if(coordL < len(input)-1):
        for c in range(coordCStart, coordCEnd+1):
            if(is_symbol(input[coordL+1][c])):
                return True
    return False

def engine_schematic(lines):

    # Accumulator
    result = 0

    # Number anchor coords
    num_coords = None

    # Current parsed number
    num = ""

    # For each coordinate, if it's a digit, then parse the "num" variable
    # by continuing to sweep. On the FIRST digit of the number, set coordL
    # and coordC to the coordinate, as your anchor point, otherwise don't touch them.
    # If the coordinate is NOT a digit, then reset the anchor coordC, reset the parsed num,
    # and check if the parsed number (given the known starting coords and number size)
    # has an adjacent symbol. If so, add it to the accumulator.
    # At the end of each line, reset the anchor anyway.
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x].isdigit():
                if num == "":
                    num_coords = (x, y)
                num += lines[y][x]
            elif num != "":
                b = has_adjacent_symbol(num_coords, num)
                if b:
                    result += int(num)
                num = ""
        if num != "":
            b = has_adjacent_symbol(num_coords, num)
            if b:
                result += int(num)
        num = ""
    return result

print(engine_schematic(input))

#  527494
#  527494
#  527364
# That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again.
