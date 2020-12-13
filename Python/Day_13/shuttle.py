from sympy.ntheory.modular import crt

def leave_time(buses, start_time):
    found = False
    time = start_time
    bus_id = None
    while not found:
        for bus in buses:        
            if time % bus == 0:
                bus_id = bus
                found = True
                break
        else:
            time += 1
            continue
    depart_time = (time - start_time) * bus_id
    return depart_time


def part2(buses):
    modulos = []
    remainders = []
    for i in range(len(buses)):
        if buses[i] == 'x':
            continue
        bus = int(buses[i])
        modulos.append(bus)
        remainders.append(bus - i)
        print(bus, bus - i)
    return crt(modulos, remainders)

with open('./test.txt') as f:
    data = f.read().split('\n')

time, buses = data
buses = buses.split(',')
orig_buses = buses
buses = [int(x) for x in buses if x.isdigit()]
time = int(time)

#print(leave_time(buses, time))
print(part2(orig_buses))

    