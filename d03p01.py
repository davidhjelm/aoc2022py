def find_double(input):
    first = input[: int(len(input) / 2)]
    second = input[int(len(input) / 2) :]

    for c in first:
        if c in second:
            if c.isupper():
                return ord(c) - 38
            else:
                return ord(c) - 96


sum = 0

f = open("d03", "r")
for line in f.readlines():
    sum += find_double(line)

print(sum)
