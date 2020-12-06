import math

def search(data, left, right, start, end):
    mid = (start + end) // 2
    for ch in data:
        if ch == left:
            end = mid
        elif ch == right:
            start = mid + 1
        mid = (start + end) // 2
    return mid

def find_missing(sortedList):
    return [x for x in range(sortedList[0], sortedList[-1]+1) 
                if x not in sortedList]

def boarding(data, partTwo=False):
    result = None
    maxID = -1
    seatIDs = []
    for d in data:        
        rowNum = search(d[:7], 'F', 'B', 0, 127)
        colNum = search(d[7:], 'L', 'R', 0, 7)
        seatID = rowNum * 8 + colNum
        seatIDs.append(seatID)
        maxID = max(maxID, seatID)
    result = maxID
    if partTwo:
        seatIDs.sort()
        result = find_missing(seatIDs)
    return result

with open('./input.txt') as f:
    data = f.readlines()
    
print(boarding(data))
print(boarding(data, True))
