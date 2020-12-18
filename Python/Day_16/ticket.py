# really did not feel like paring the input today....

rules = {
    'dl': [40,261,279,955],
    'ds': [33,375,394,963],
    'dp': [39,863,877,970],
    'dt': [30,237,256,955],
    'dd': [47,731,741,950],
    'dti': [38,301,317,954],
    'al': [26,598,623,969],
    'as': [50,835,854,971],
    'ap': [44,535,549,958],
    'at': [36,672,685,967],
    'c': [34,217,236,974],
    'd': [29,469,483,970],
    'p': [45,111,120,965],
    'ru': [32,751,760,954],
    'r': [25,321,339,954],
    's': [38,423,438,958],
    'tr': [45,798,813,954],
    'ty': [40,487,503,954],
    'w': [46,916,938,949],
    'z': [25,160,184,957]
}
def is_valid(type, ll, lh, hl, hh, val):
    if (ll <= val <= lh) or (hl <= val <= hh):
        return True
    return False

invalid = []
def validate(ticket):
    
    for nums in ticket: 
        temp = [int(x) for x in nums.split(',')]   
        for t in temp:    
            valid = False
            #print(num)
            for k, v in rules.items():
                #print(k, v[0], v[1], v[2], v[3], num)
                if is_valid(k, v[0], v[1], v[2], v[3], t):               
                    valid = True
                    break
            if not valid:
                invalid.append(t)
    return sum(invalid)
            


with open('./test.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    print(lines)

print(validate(lines))