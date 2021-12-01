from input_parser import parse_input

in_ = parse_input("day1/part1.txt")
in_ = [int(i) for i in in_]

output = [
    1 for i in range(1, len(in_))
    if int(in_[i]) > int(in_[i-1])
]

print(len(output))