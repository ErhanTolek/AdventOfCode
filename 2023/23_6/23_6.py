import os


def read_input_file_lines():
    with open(os.path.dirname(__file__) + "/input.txt") as file:
        lines = file.read().strip()
        return lines

def f_1():
    lines = read_input_file_lines()
    time_values = []
    distance_values = []
    _count = 1
    for line in lines.split('\n'):
        if line.startswith('Time:'):
            time_values = [int(x) for x in line.split()[1:]]
        elif line.startswith('Distance:'):
            distance_values = [int(x) for x in line.split()[1:]]

    for i in range(len(time_values)):
        rs = int(time_values[i])
        ds = int(distance_values[i])
        count = 0
        for c in range(int(rs)):
            hs = c+1
            if (rs - hs)*hs > ds:
                count += 1
        _count *= count
    print(_count)
def f_2():
    lines = read_input_file_lines()
    time_values = []
    distance_values = []
    _count = 1
    for line in lines.split('\n'):
        if line.startswith('Time:'):
            time_values = [int(x) for x in line.split()[1:]]
        elif line.startswith('Distance:'):
            distance_values = [int(x) for x in line.split()[1:]]
    time_value = [''.join(map(str, time_values))]
    distance_value = [''.join(map(str, distance_values))]
    _count = 1
    rs = int(time_value[0])
    ds = int(distance_value[0])
    count = 0
    for c in range(int(rs)):
        hs = c+1
        if (rs - hs)*hs > ds:
            count += 1
    _count *= count
    print(_count)
if __name__ == '__main__':
    f_2()