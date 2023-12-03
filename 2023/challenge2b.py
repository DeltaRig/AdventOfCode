# --- Part Two ---
# The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

# As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

# Again consider the example games from earlier:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

def powerSetGame(revealed_sets):
    # Initialize counts for each cube color
    counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    # Update counts based on the revealed sets
    for set_str in revealed_sets:

        cubes = set_str.split(',')
        for cube in cubes:
            cube = cube.strip().split(' ')
            
            color = cube[-1]  # Last element in the list is the color
            if counts[color] < int(cube[0]):
                counts[color] = int(cube[0])
            # Check if the counts match the target cube counts

    # print("Red: ", counts['red'],"Green: ", counts['green'],"Blue: ", counts['blue'] ) 
    mul =  counts['red'] * counts['green'] * counts['blue']   
    # print("Mul " , mul)
    return mul

def power_games_sum(games):
    # Initialize a list to store possible game IDs
    power_of_set = []

    # Iterate through each game
    for game in games:
        # Split the game information into ID and revealed sets
        game_info = game.split(':')
        game_id = int(game_info[0].split()[-1])

        revealed_sets = game_info[1].strip().split(';')  #strip == trim

        power_of_set.append(powerSetGame(revealed_sets))

    # Calculate the sum of possible game IDs
    sum_of_power_of_set = sum(power_of_set)

    return sum_of_power_of_set

# Example games
input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
input = open("challenge2b.txt", "r")

# Calculate the sum of IDs of possible games
result = power_games_sum(input)

# Print the result
print("The sum of power of the set games is:", result)

