import re

# Function to parse the input file and extract data
def parse_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        seeds = list(map(int, lines[0].strip().split()[1:]))
        maps = {}
        current_map = "None"
        print("LINNES ", lines[1:])
        for line in lines[1:]:
            if line.startswith('seed-to-soil'):
                current_map = 'seed-to-soil'
                maps[current_map] = []
            elif line.startswith('soil-to-fertilizer'):
                current_map = 'soil-to-fertilizer'
                maps[current_map] = []
            elif line.startswith('fertilizer-to-water'):
                current_map = 'fertilizer-to-water'
                maps[current_map] = []
            elif line.startswith('water-to-light'):
                current_map = 'water-to-light'
                maps[current_map] = []
            elif line.startswith('light-to-temperature'):
                current_map = 'light-to-temperature'
                maps[current_map] = []
            elif line.startswith('temperature-to-humidity'):
                current_map = 'temperature-to-humidity'
                maps[current_map] = []
            elif line.startswith('humidity-to-location'):
                current_map = 'humidity-to-location'
                maps[current_map] = []
            else:
                values = re.findall(r'\d', line)
                print("new line ",line)
                for value in values:
                    maps[current_map].append(value)
        return seeds, maps


# Parse the input file
seeds, maps = parse_input_file('challenge5.txt')
print("SEEDS " ,seeds)
print("MAPS " ,maps)

lowest_location_number = float('inf')