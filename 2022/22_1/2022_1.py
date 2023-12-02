import os


def read_input_file_lines():
    with open(os.path.dirname(__file__)+"/input.txt") as file:
        lines = file.readlines()
        return lines

def sum_of_cal():
    lines = read_input_file_lines()
    calorieList = []
    _sum = 0
    topThreeSum = 0
    for line in lines:
        if not line[0].strip() == "":
            _sum += int(line)
        else:
            calorieList.append(_sum)
            _sum=0
    for i in range(3):
        print(i)
        topThreeSum += max(calorieList)
        calorieList.remove(max(calorieList))
    print(topThreeSum)

if __name__ == '__main__':
    sum_of_cal()