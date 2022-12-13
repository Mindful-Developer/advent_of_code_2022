import math


with open("ch_11", "r") as f:
    data = f.read().splitlines()
    data = [line for line in data if line]

class Monkey:
    __slots__ = ('items', 'operation', 'div_pass', 'div_fail', '_insp_count', '_div')
    def __init__(self, starters, operation, div, div_pass, div_fail):
        self.items = starters
        self.operation = operation
        self.div_pass = div_pass
        self.div_fail = div_fail
        self._insp_count = 0
        self._div = div

    @property
    def inspection_count(self):
        return self._insp_count

    @property
    def divisor(self):
        return self._div

    def catch(self, item):
        self.items.append(item)

    def apply_worry(self, old):
        return eval(self.operation)

    def has_items(self):
        return len(self.items) > 0

    def inspect_item(self, worry_div):
        self._insp_count += 1
        item = self.items.pop(0)
        worry = self.apply_worry(item)
        boredom = worry // worry_div
        target = (
            self.div_pass
            if boredom % self.divisor == 0
            else self.div_fail
        )
        return target, boredom


def monkey_factory(lines):
    result = []
    for index in range(0, len(lines), 6):
        monkey_slice = lines[index : index + 6][1:]
        items = [int(v.strip()) for v in monkey_slice[0].split(":")[1].split(",")]
        operation = monkey_slice[1].split("=")[1].strip()
        div = int(monkey_slice[2].split(" ")[-1])
        div_pass = int(monkey_slice[3].split(" ")[-1])
        div_fail = int(monkey_slice[4].split(" ")[-1])
        monkey = Monkey(starters=items, operation=operation, div=div, div_pass=div_pass,
                        div_fail=div_fail)
        result.append(monkey)

    return result


def first_part(rounds):
    monkeys = monkey_factory(data)

    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.has_items():
                target_monkey, item = monkey.inspect_item(worry_div=3)
                monkeys[target_monkey].catch(item)

    insp_count = sorted([m.inspection_count for m in monkeys])
    return insp_count[-2] * insp_count[-1]


def second_part(rounds):
    monkeys = monkey_factory(data)
    lcm = math.lcm(*[m.divisor for m in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.has_items():
                target_monkey, item = monkey.inspect_item(worry_div=1)
                item = item % lcm
                monkeys[target_monkey].catch(item)

    insp_counts = sorted([m.inspection_count for m in monkeys])
    return insp_counts[-2] * insp_counts[-1]


if __name__ == "__main__":
    print(first_part(rounds=20), second_part(rounds=10_000))