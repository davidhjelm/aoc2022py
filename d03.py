def get_unique(input):
    return list(dict.fromkeys((input)))


def find_badge(input):
    lines = input.splitlines()
    chars = get_unique(lines[0])
    # print(chars)

    newchars = list()

    for c in lines[1]:
        if c in chars:
            newchars.append(c)

    newchars = get_unique(newchars)
    newchars2 = list()

    for c in lines[2]:
        if c in newchars:
            newchars2.append(c)

    # print(newchars2)

    c = get_unique(newchars2)[0]

    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96


sum = 0

f = open("inputs/d03", "r")

# testlines = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg"""

# print(find_badge(testlines))

# for line in testlines.split("\n")[:3]:
count = 0
lines = ""
for line in f.readlines():
    if count < 3:
        count += 1
        lines += line
    else:
        count = 1
        sum += find_badge(lines)
        lines = line

sum += find_badge(lines)
print(sum)
