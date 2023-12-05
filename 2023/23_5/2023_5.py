import os

def read_input_file_lines():
    with open(os.path.dirname(__file__) + "/input.txt") as file:
        lines = file.read().strip()
        return lines

def f_1():
    lines = read_input_file_lines()
    _count = 0
    for line in lines.split('\n'):
        _id, cardLine = line.split(":")
        winNs, myNs = cardLine.split("|")
        myN = [item for item in myNs.split(" ") if item.strip()]
        winN = [item for item in winNs.split(" ") if item.strip()]
        common_elements = len([element for element in myN if element in winN])
        if common_elements > 0:
            points = pow(2, common_elements - 1)
            _count += points
            print(_count)
def f_2():
    lines = read_input_file_lines()
    _count = 0
    copyList = []
    sum = 0
    for line in lines.split('\n'):
        _id, cardLine = line.split(":")
        _id = int(_id.split(" ")[-1])
        winNs, myNs = cardLine.split("|")
        myN = [item for item in myNs.split(" ") if item.strip()]
        winN = [item for item in winNs.split(" ") if item.strip()]
        common_elements = len([element for element in myN if element in winN])
        for i in range(_id+1,_id+common_elements+1):
            copyList.append(i)

        if _id in copyList:
            for _ in range(copyList.count(_id)):
                for i in range(_id + 1, _id + common_elements + 1):
                    copyList.append(i)

    for card in range(2,max(copyList)+1):
        count = copyList.count(card) + 1
        sum += count
    print(sum+1)


if __name__ == '__main__':
    f_2()