from input_parser import parse_input

in_ = parse_input("day1/part2.txt")
in_ = [int(i) for i in in_]

windows = [
    in_[i] + in_[i-1] + in_[i-2]
    for i in range(2, len(in_))
]

output = [
    1 for i in range(1, len(windows))
    if windows[i] > windows[i-1]
]

print(len(output))
