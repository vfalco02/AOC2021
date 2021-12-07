from input_parser import parse_input


def test_part_1():
    in_ = parse_input("input.txt")
    most = least = ''
    for i in range(0, len(in_[0])):
        count = {'0': 0, '1': 0}
        for row in in_:
            count[row[i]] += 1
        most += max(count, key=count.get)
        least += min(count, key=count.get)

    print(int(most, 2) * int(least, 2))


def test_part_2():
    in_ = parse_input("input.txt")
    ratings = {"oxygen": [i for i in in_], "co2": [i for i in in_]}
    for i in range(0, len(in_[0])):
        count = {'0': 0, '1': 0}
        for row in ratings["oxygen"]:
            count[row[i]] += 1
        if count['0'] == count['1']:
            most = "1"
        else:
            most = max(count, key=count.get)
        print(f"Most is {most}")
        tmp = [row for row in ratings["oxygen"] if row[i] == most]
        ratings["oxygen"] = [row for row in tmp]
        if len(tmp) == 1: break

    for i in range(0, len(in_[0])):
        count = {'0': 0, '1': 0}
        for row in ratings["co2"]:
            count[row[i]] += 1
        if count['0'] == 0 or count['1'] == 0:
            continue
        if count['0'] == count['1']:
            least = "0"
        else:
            least = min(count, key=count.get)
        print(f"Least is {least}")
        tmp = [row for row in ratings["co2"] if row[i] == least]
        ratings["co2"] = [row for row in tmp]
        if len(tmp) == 1: break

    print(int(ratings["oxygen"][0], 2) * int(ratings["co2"][0], 2))

