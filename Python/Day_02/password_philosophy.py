import re

def validate(low, high, char, passCode):
    count = passCode.count(char)
    if low <= count <= high:
        return 1
    return 0

def validate2(pos1, pos2, char, passCode):
    # exclusively one or the other: XOR  bool(a) ^ bool(b)
    if (passCode[pos1-1] == char) ^ (passCode[pos2-1] == char):
        return 1
    return 0

def password_validator(data, partTwo=False):
    valid_count = 0
    for line in data:
        num1,num2 = [int(x) for x in line[0].split('-')]
        char = line[1].strip(':')
        passCode = line[2]     
        if partTwo:
            valid_count += validate2(num1, num2, char, passCode)
        else:   
            valid_count += validate(num1, num2, char, passCode)
    return valid_count

if __name__ == "__main__":
    data = []
    with open('./input.txt') as f:
        for line in f:
            data.append(line.split())
    res = password_validator(data)
    res2 = password_validator(data, partTwo=True)
    print('Part One: ',res)
    print('Part Two: ',res2)

