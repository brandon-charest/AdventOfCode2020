data = []
with open('./input.txt') as f:
    temp = ''
    for line in f.readlines():    
        if line != '\n':
            temp += line.replace('\n', '')
        else:
            data.append(temp)
            temp = ''
    data.append(temp)
    sum = 0
    for d in data:
        sum += len(set(d))
print(sum)