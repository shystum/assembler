from sys import argv

input_file = argv[1]
instructions = []

with open(input_file) as file:
    instructions = file.readlines()

# clean whitespaces
instructions = [i.strip() for i in instructions]

print(instructions)

