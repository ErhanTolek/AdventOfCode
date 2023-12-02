import os


def read_input_file_lines():
    with open(os.path.dirname(__file__)+"/1_input.txt") as file:
        lines = file.readlines()
        return lines

def find_calibration_value():
    ans=0
    lines = read_input_file_lines()
    for line in lines:
        digits = []
        for i,c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d,val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
                if line[i:].startswith(val):
                    digits.append(str(d+1))
        score = int(digits[0] + digits[-1])
        ans += score
    print(ans)


if __name__ == '__main__':
    find_calibration_value()