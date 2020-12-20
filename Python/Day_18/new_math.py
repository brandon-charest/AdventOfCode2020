
def op(stack, num):
    while stack:
        if stack[-1] == '(':
            break
        operator, left_op = stack[-1], stack[-2]
        stack = stack[:-2]
        if operator == '+':
            num = left_op + num
        elif operator == '*':
            num = left_op * num

    stack.append(num)
    return stack


def calc(exp):
    stack = []
    idx = 0
    while idx < len(exp):
        curr = exp[idx]
        if curr.isnumeric():
            num = int(curr)
            stack = op(stack, num)

        elif curr in '*+(':
            stack.append(curr)

        elif curr == ')':
            num = int(stack[-1])            
            stack = stack[:-2]  
            stack = op(stack, num)
        idx += 1 

    return int(stack[0])


def part1(exps):
    ans = 0
    for exp in exps:
        ans += calc(exp)
    return ans

with open('./input.txt') as f:
    data = f.read().split('\n')
print(part1(data))