import os
from collections import defaultdict


def read_input_file_lines():
    with open(os.path.dirname(__file__) + "/input.txt") as file:
        lines = file.readlines()
        return lines


def sol_1():
    lines = read_input_file_lines()
    missMatch = []
    V = defaultdict(int)
    for line in lines:
        _id, rest_line = line.split(':')
        for turn in rest_line.split(';'):
            for balls in turn.split(','):
                count, color = balls.split()
                _count = int(count)
                V[color] = _count
                if {'red': 12, 'green': 13, 'blue': 14}.get(color) < V[color]:
                    a, l = _id.split(" ")
                    missMatch.append(int(l))

    print(sum(range(0, 101)) - sum(set(missMatch)))


def sol_2():

    lines = read_input_file_lines()
    _sum = 0
    a = defaultdict(list)
    for line in lines:
        _id, rest_line = line.split(':')
        for turn in rest_line.split(';'):
            for balls in turn.split(','):
                count, color = balls.split()
                a[color].append(int(count))
        b = max(a['blue'])*max(a['red'])*max(a['green'])
        _sum += b
        a = defaultdict(list)
    print(_sum)

if __name__ == '__main__':
    sol_2()

