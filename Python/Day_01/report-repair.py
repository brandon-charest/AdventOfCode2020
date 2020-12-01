import re

def ReportRepair(dataList):
    for i in range(0, len(dataList)):
        for j in range(i+1, len(dataList)):
            num1, num2 = dataList[i], dataList[j]
            if num1 + num2 == 2020:
                return num1 * num2

def ReportRepair2(dataList):
    for i in range(0, len(dataList)):
        for j in range(i+1, len(dataList)):
            for k in range(j+1, len(dataList)):
                num1, num2, num3 = dataList[i], dataList[j], dataList[k]
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

if __name__ == "__main__":
    with open('./input.txt') as f:
        data = f.read().split()
        data = list(map(int, data))  
    result = ReportRepair2(data)
    print(result)