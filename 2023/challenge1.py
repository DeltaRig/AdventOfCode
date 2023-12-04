# /**
#  * https://adventofcode.com/2023/day/1
#  * 
#  * @author (Daniela Pereira Rigoli)
#  * @version (02/12/2023)
#  */
# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?
import re

def extract_calibration_value(line):
    # Use regex to find all digits in the line
    digits = re.findall(r'\d', line)
    
    if digits:
        # Extract the first and last digits from the list of digits
        first_digit = digits[0]
        last_digit = digits[-1]
        
        # Calculate the calibration value
        calibration_value = int(first_digit + last_digit)
        return calibration_value

    # Return 0 or handle it differently based on your needs
    return 0

def sum_of_calibration_values(calibration_document):
    # Split the document into lines and calculate the calibration values
    calibration_values = [extract_calibration_value(line) for line in calibration_document]
    
    # Sum up all calibration values
    total_sum = sum(calibration_values)
    
    return total_sum

# Example calibration document
# calibration_document = [
#     "1abc2",
#     "pqr3stu8vwx",
#     "a1b2c3d4e5f",
#     "treb7uchet"
# ]

calibration_document = open("challenge1.txt", "r")


# Calculate the sum of calibration values
result = sum_of_calibration_values(calibration_document)

# Print the result
print("The sum of all calibration values is:", result)
