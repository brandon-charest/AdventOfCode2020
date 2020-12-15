def mem_game(start, end):
    last = {}
    curr, prev = 0, None
    for i in range(len(start)):
        last[start[i]] = i
    for i in range(len(start), end):
        prev = curr
        if curr not in last.keys():
            curr = 0
        else:
            curr = i - last[curr]
        last[prev] = i
    #print(last)
    return prev


print(mem_game([8,13,1,0,18,9], 30000000))