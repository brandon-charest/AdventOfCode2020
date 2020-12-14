from collections import defaultdict
import re


def to_binary(num):
    return '{0:036b}'.format(num)


def to_int(binary):
    return int(binary, 2)


def parse_instr(line):
    addr = re.findall(r'(?<=\[)\d+', line)
    val = re.findall(r'(?<=\=\s).+', line)
    val = int(val[0])
    binary = list(to_binary(val))
    return int(addr[0]), binary


curr_mask = None
def calc_docking_data(data):
    for line in data:
        if 'mask' in line:
            curr_mask = line.replace('mask = ', '')
            continue
        addr, b_list = parse_instr(line)
        for i in range(len(curr_mask)):
            if curr_mask[i].isnumeric():
                b_list[i] = curr_mask[i]
        res = to_int(''.join(b_list))
        #print(''.join(b_list))
        #print(curr_mask)
        #print(res)
        mem[addr] = res
    ans = 0
    for k in mem.keys():
        ans += mem[k]
    print(ans)

mem = defaultdict()

with open('./input.txt') as f:
    data = f.read().split('\n')

calc_docking_data(data)

 
