import os


def read_input_file_lines():
    with open(os.path.dirname(__file__)+"/input.txt") as file:
        lines = file.readlines()
        return lines

def functions():
    lines = read_input_file_lines()
    _sum = 0
    for line in lines:
        firstChoise = int(ord(line[0])) - 64
        secondChoise = int(ord(line[2])) - 87
        _sum += secondChoise
        if secondChoise == 1 and firstChoise == 3:
            _sum += 6
        elif secondChoise == 3 and firstChoise == 1:
            _sum += 0
        else:
            if secondChoise > firstChoise:
                _sum += 6
            elif secondChoise == firstChoise:
                _sum += 3
            elif secondChoise < firstChoise:
                _sum += 0
    print(_sum)

def functions2():
    lines = read_input_file_lines()
    _sum = 0
    sum2 = 0
    secondChoise = 0
    resultP = 0
    for line in lines:

        firstChoise = int(ord(line[0])) - 64
        result = int(ord(line[2])) - 87
        if result == 3:
            resultP = 6
            if firstChoise == 1:
                secondChoise = 2
            elif firstChoise == 2:
                secondChoise = 3
            else:
                secondChoise = 1
            _sum += secondChoise + resultP
        elif result == 2:
            resultP = 3
            if firstChoise == 1:
                secondChoise = 1
            elif firstChoise == 2:
                secondChoise = 2
            else:
                secondChoise = 3
            _sum += secondChoise + resultP
        else:
            resultP = 0
            if firstChoise == 1:
                secondChoise = 3
            elif firstChoise == 2:
                secondChoise = 1
            else:
                secondChoise = 2
            _sum += secondChoise + resultP

    print(_sum)


if __name__ == '__main__':
    functions()
    functions2()


