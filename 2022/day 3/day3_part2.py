from day3 import rucksacks, alphabet
import re

group_rucksacks = [rucksacks[x:x + 3] for x in range(0, len(rucksacks), 3)]

priority = 0
pattern = r"[{''}]"

for group in group_rucksacks:
    badge = set(group[0]).intersection(set(group[1]), set(group[2]))

    if badge != set():
        priority += alphabet.index(re.sub(pattern, "", str(badge))) + 1

print(priority)  
