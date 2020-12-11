with open("./test.txt") as f:
    data = f.read().split("\n")
    data = [int(x) for x in data]
    data.append(0)
    data.sort()
    data.append(max(data) + 3)


threes = 0
ones = 0

for i in range(1, len(data)):
    diff = data[i] - data[i - 1]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1


print(f"{ones} * {threes} = {ones*threes}")

DP = {}


def dp(i):
    if i == len(data) - 1:
        return 1

    if i in DP:
        return DP[i]

    res = 0
    for j in range(i + 1, len(data)):
        if data[j] - data[i] <= 3:
            res += dp(j)
    DP[i] = res
    return res


print(dp(0))