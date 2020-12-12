
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'
FORWARD = 'F'
LEFT = 'L'
RIGHT = 'R'

directions = {
    NORTH: [0, 1],
    EAST: [1, 0],
    SOUTH: [0, -1],
    WEST: [-1, 0]
}

def right_rotate(pos, amt):
    x,y = pos
    if amt % 360 == 0:
        return x, y
    elif amt % 360 == 90:
        return y, -x
    elif amt % 360 == 180:
        return -x, -y
    elif amt % 360 == 270:
        return [-y, x]

 # can reuse right rotate  
def left_rotate(pos, amt):
    return right_rotate(pos, 360 - amt)

def ship1(instr):
    curr_direction = directions[EAST]
    curr_pos =[0,0]

    for line in instr:
        code = line[0]
        move = int(line[1:])
        if code == FORWARD:            
            curr_pos[0] += curr_direction[0] * move
            curr_pos[1] += curr_direction[1] * move            
        elif code in directions.keys():
            curr_pos[0] += directions[code][0] * move
            curr_pos[1] += directions[code][1] * move          
        elif code == LEFT:
            curr_direction = left_rotate(curr_direction, move)
        elif code == RIGHT:
            curr_direction = right_rotate(curr_direction, move)
    
    return abs(curr_pos[0]) + abs(curr_pos[1])


def ship2(instructions):
    curr_pos = [0, 0]
    curr_way = [10, 1]

    for line in data:
        code, val = line[0], int(line[1:])
        if code == FORWARD:            
                curr_pos[0] += curr_way[0] * val
                curr_pos[1] += curr_way[1] * val            
        elif code in directions.keys():
            curr_way[0] += directions[code][0] * val
            curr_way[1] += directions[code][1] * val
        elif code == LEFT:
            curr_way = list(left_rotate(curr_way, val))
        elif code == RIGHT:
            curr_way = list(right_rotate(curr_way, val))
    return abs(curr_pos[0]) + abs(curr_pos[1])


with open('./input.txt') as f:
    data = f.read().split('\n')

print(ship1(data))
print(ship2(data))
