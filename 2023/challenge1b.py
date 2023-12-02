# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?
import re

# Dictionary to map spelled-out digits to numeric values
digit_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def extract_calibration_value(line):
    # Use regex to find all spelled-out digits or numeric digits in the line
    digits = re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', line)
    
    if digits:
        # Extract the first and last digits from the list of digits
        first_digit = digits[0]
        last_digit = digits[-1]
        print(last_digit)

        # If the first digit is spelled out, map it to the corresponding numeric value
        if first_digit in digit_mapping:
            first_digit = digit_mapping[first_digit]

        # If the last digit is spelled out, map it to the corresponding numeric value
        if last_digit in digit_mapping:
            last_digit = digit_mapping[last_digit]

        # Calculate the calibration value
        calibration_value = int(first_digit + last_digit)
        print(calibration_value)
        return calibration_value

    # Return 0 or handle it differently based on your needs
    return 0

def sum_of_calibration_values(calibration_document):
    # Split the document into lines and calculate the calibration values
    calibration_values = [extract_calibration_value(line) for line in calibration_document]

    # Sum up all calibration values
    total_sum = sum(calibration_values)

    return total_sum

# # Example calibration document for Part Two
calibration_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen", # 281
    "rjsevenonefllcrdnbmqcmxqsq38", #78
    "twoseven2dppxgmlhr61onenine4", #24
    "sevenb3btzhscqbrxxjkhtzpv", # 73
    "859two", # 82
    "one1",
    "391"
]
# calibration_document = open("challenge1b.txt", "r")

# Calculate the sum of calibration values for Part Two
result = sum_of_calibration_values(calibration_document)

# Print the result for Part Two
print("The sum of all calibration values for Part Two is:", result)

# tries: 53293
# That's not the right answer; your answer is too low. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again.