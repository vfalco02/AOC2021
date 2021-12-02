from input_parser import parse_input

in_ = parse_input("day2/part1.txt")

horizontal = 0
depth = 0

for command in in_:
    split_command = command.split(' ')
    if split_command[0] == "forward":
        horizontal += int(split_command[1])
    elif split_command[0] == "up":
        depth -= int(split_command[1])
    elif split_command[0] == "down":
        depth += int(split_command[1])

print(horizontal, depth, horizontal*depth)