import math


class Item:
    def __init__(self, worry):
        self.worry = worry


class Monkey:
    inspections = 0

    def run(self, monkeys):
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.inspections += 1

            if self.operation[0] == "*":
                if self.operation[1] == "old":
                    item.worry *= item.worry
                else:
                    item.worry *= int(self.operation[1])
            if self.operation[0] == "+":
                item.worry += int(self.operation[1])

            item.worry %= math.lcm(*[m.test for m in monkeys])

            if item.worry % self.test == 0:
                monkeys[self.iftrue].items.append(item)
            else:
                monkeys[self.iffalse].items.append(item)


monkeys = []

f = open("inputs/d11", "r")

monkey = Monkey()
items = []
for line in f.readlines():
    line = line.lstrip()
    if line.startswith("Starting"):
        for p in line.split(": ")[1:]:
            for w in p.split(", "):
                if len(w) > 0:
                    items.append(Item(int(w)))
    if line.startswith("Operation"):
        for p in line.split("old ")[1:]:
            p = p.strip()
            monkey.operation = (p.split(" ")[0], p.split(" ")[1])
    if line.startswith("Test"):
        for p in line.split("by ")[1:]:
            monkey.test = int(p)
    if line.startswith("If true"):
        for p in line.split("monkey ")[1:]:
            monkey.iftrue = int(p)
    if line.startswith("If false"):
        for p in line.split("monkey ")[1:]:
            monkey.iffalse = int(p)
    if len(line) == 0:
        monkey.items = items
        monkeys.append(monkey)
        monkey = Monkey()
        items = []

monkey.items = items
monkeys.append(monkey)

for i in range(10000):
    for m in monkeys:
        m.run(monkeys)


result = sorted((m.inspections for m in monkeys), reverse=True)[:2]
print(result[0] * result[1])
