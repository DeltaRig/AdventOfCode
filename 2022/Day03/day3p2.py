
# Daniela Pereira Rigoli
# August 13th 2024
# https://adventofcode.com/2022/day/3
# part2
            
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def priority(letter):
    return ord(letter) - 96 if ord(letter) > 96 else ord(letter) - 38


def rucksack(groups):
    result = 0
    
    for i in range(0, len(groups), 3):
        # Extract the three rucksacks for the current group
        rucksack1 = set(groups[i])
        rucksack2 = set(groups[i + 1])
        rucksack3 = set(groups[i + 2])
        
        # Find the common item in all three rucksacks
        common_item = rucksack1 & rucksack2 & rucksack3
        if common_item:
            badge_item = common_item.pop()
            result += priority(badge_item)
    return result

rucksacks = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

result = 0
f = open("input.txt", "r").read().splitlines()
result = rucksack(f)
print("Sum of the priorities of badge items:", result)


# Find the sum of the priorities of the badge items
result = rucksack(rucksacks)
print("Sum of the priorities of badge items:", result)


print(result)
