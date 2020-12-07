import re
from collections import defaultdict

contained_in = defaultdict(set)
contains = defaultdict(list)
has_gold = set()


def find_gold(color):    
    for c in contained_in[color]:
        has_gold.add(c)
        find_gold(c)

def count_contained(src, cache={}):
    if src in cache:
        return cache[src]
    total = 0

    for count, color in contains[src]:
        total += count
        total += count * count_contained(color)
    cache[src] = total
    return total

with open('./input.txt') as f:
    data = f.read().split('\n')
    for line in data:
        color = re.match(r'(.+?) bags contain', line).group(1)
        for count, child_color in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            count = int(count)
            contained_in[child_color].add(color)
            contains[color].append((count, child_color))


find_gold('shiny gold')
print(len(has_gold))
print(count_contained('shiny gold'))



