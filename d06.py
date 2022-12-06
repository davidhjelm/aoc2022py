def get_unique(input):
    return list(dict.fromkeys((input)))


def get_marker(input):
    count = 0
    chars = []
    for c in list(input):
        count += 1
        chars.append(c)
        if len(chars) == 4:
            if len(get_unique(chars)) != 4:
                chars.pop(0)
            else:
                return count


f = open("inputs/d06", "r")

print(get_marker(f.readline()))
