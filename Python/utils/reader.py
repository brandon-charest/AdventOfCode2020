import re

def input_reader(path):
    with open(path) as f:
        data = f.read().split()
    return data