import re

stacks = {}

testinput = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

f = open("inputs/d05", "r")

build_stack = True
for line in f.readlines():
    inc = 1
    chars = list(line)
    try:
        if chars[1] == "1":
            build_stack = False
    except IndexError:
        pass
    if build_stack == True:
        for i, c in enumerate(chars):
            if i % 4 == 1:
                if c.strip() != "":
                    if inc in stacks.keys():
                        stacks[inc] += c
                    else:
                        stacks.update({inc: [c.strip()]})
                inc += 1

    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    if m is not None:
        amount = int(m.group(1))
        src = int(m.group(2))
        dst = int(m.group(3))

        flipped = stacks[src][:amount]
        flipped.reverse()
        stacks[dst] = flipped + stacks[dst]
        stacks[src] = stacks[src][amount:]

for i, s in enumerate(stacks, start=1):
    print(stacks[i][0], end="")

print()
