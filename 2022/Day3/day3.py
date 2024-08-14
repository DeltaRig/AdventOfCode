
# Daniela Pereira Rigoli
# August 11th 2024
# https://adventofcode.com/2022/day/3

# O(n^2)
# O(max line/2)
def findMatch(line):
    list = set()
    compSize = int((len(line))/2)
    for a in line[:compSize]:
        for b in line[compSize:]:
            if a == b:
                list.add(a)
    return list
            
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def priority(letter):
    return ord(letter) - 96 if ord(letter) > 96 else ord(letter) - 38

result = 0
f = open("input.txt", "r")
for line in f:
    match = findMatch(line)
    for a in match:
        # print(a,  " | " , priority(a))
        result += priority(a)

print(result)


f.close()
