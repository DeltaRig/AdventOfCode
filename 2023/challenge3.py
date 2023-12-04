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

def is_symbol(a):
    return a != '.' and not a.isdigit()

def adjacent_symbol(coordL, coordC, num):
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

def engine_schematic():
    result = 0
    coordC = -1
    coordL = -1
    num = ""
    for line in range(0, len(input)):
        for colunm in range(0, len(input[0])):
            if(input[line][colunm].isdigit()):
                num += input[line][colunm]
                if(coordC == -1):
                    coordL = line
                    coordC = colunm
            else:
                if(coordC != -1):
                    adj = adjacent_symbol(coordL, coordC, num)
                    if(adj):
                        result += int(num)
                    coordC = -1
                    num = ""
        coordC = -1
    return result
print(len(input))
print(len(input[0]))

print(engine_schematic())

#  527494
#  527494
# That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again.
