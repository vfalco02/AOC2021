from input_parser import parse_input

in_ = parse_input("day2/part2.txt")

horizontal = 0
depth = 0
aim = 0

for command in in_:
    split_command = command.split(' ')
    if split_command[0] == "forward":
        horizontal += int(split_command[1])
        depth += aim * int(split_command[1])
    elif split_command[0] == "up":
        aim -= int(split_command[1])
    elif split_command[0] == "down":
        aim += int(split_command[1])

print(horizontal, depth, horizontal*depth)