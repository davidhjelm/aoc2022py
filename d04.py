sum = 0

f = open("inputs/d04", "r")

testlines = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
3-82,24-83"""

for line in f.readlines():
    # for line in testlines.splitlines():
    f = line.split(",")[0]
    s = line.split(",")[1].strip()

    f1 = int(f.split("-")[0])
    f2 = int(f.split("-")[1])

    s1 = int(s.split("-")[0])
    s2 = int(s.split("-")[1])

    if s1 < f1:
        f, s = s, f
        f1 = int(f.split("-")[0])
        f2 = int(f.split("-")[1])

        s1 = int(s.split("-")[0])
        s2 = int(s.split("-")[1])

    if s1 <= f2 and s1 >= f1:
        sum += 1

print(sum)
