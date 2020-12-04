import re

required = ['ecl:', 'pid:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'hgt:']
eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def check(passport):
    for req in required:
        if req not in passport:
            return False
    return True


def _helper(param, val):

    if param == 'ecl':
        if val in eye_color:
            return True
        return False
    elif param == 'pid':
        if re.match("^(?=.{9}$)\d*$", val) is not None:
            return True
        return False
    elif param == 'eyr':
        val = int(val)
        if 2020 <= val <= 2030:
            return True
        return False
    elif param == 'hcl':
        if re.match("^#(?=.{6}$)\w*$", val) is not None:
            return True
        return False
    elif param == 'byr':
        val = int(val)
        if 1920 <= val <= 2002:
            return True
        return False
    elif param == 'iyr':
        val = int(val)
        if 2010 <= val <= 2020:
            return True
        return False
    elif param == 'hgt': 
        if re.search("(cm|in)", val):
            m = val[-2:]
            num = int(val[:-2])
            if m == 'cm':
                if 150 <= num <= 193:
                    return True
                return False
            else:
                if 59 <= num <= 76:
                    return True
        return False
    elif param =="cid":
        return True

def check2(passport):
    items = list(filter(None,passport.split(' ')))
    is_valid = True  
    for item in items:
        param, val = item.split(':')
        if not _helper(param, val):
            is_valid = False
            #print(param, val)
            break          
    return is_valid

  

def validate_passport(passport_list, partTwo=False):
    count = 0
    for p in passport_list:
        if partTwo:
            if check(p):
                if check2(p):
                    count += 1
        else:
            passport = re.findall('[\w.]+:', p)   
            if check(passport):
                count += 1
    return count


data= []
temp = ''
with open('./input.txt') as f:
    for line in f.readlines():
        if line != '\n':
            temp += line.replace('\n', ' ')            
        else:
            data.append(temp)
            temp = ''
    data.append(temp)

res = validate_passport(data, True)
print(res)        