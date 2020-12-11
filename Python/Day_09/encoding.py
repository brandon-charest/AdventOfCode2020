from collections import deque
from itertools import combinations


def find_subarray(data, target):
    curr_sum = data[0]
    start, idx = 0, 1
    size = len(data)
    while idx <= size:
        while curr_sum > target and start < idx - 1:
            curr_sum = curr_sum - data[start]
            start += 1

        if curr_sum == target:
            return data[start:idx]

        if idx < size:
            curr_sum = curr_sum + data[idx]
        idx += 1

    return None


def find_sum(list, target):
    for comb in combinations(list, 2):
        if sum(comb) == target:
            return True
    return False


def decode(data, preamble):
    window = deque()
    for i in range(len(data)):
        if len(window) < preamble:
            window.append(data[i])
        else:
            if not find_sum(window, data[i]):
                return data[i]
            window.popleft()
            window.append(data[i])


with open("./test.txt") as f:
    data = f.read().split("\n")
    data = [int(x) for x in data]

target = decode(data, 25)
print(target)
subarray = find_subarray(data, target)
subarray.sort()
print(subarray[0] + subarray[len(subarray) - 1])
