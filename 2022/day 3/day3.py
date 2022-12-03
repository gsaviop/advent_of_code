import string

input = open("input.txt", "r")
txt = input.read()

rucksacks = txt.splitlines()

input.close()

alphabet = list(string.ascii_letters)
priority = 0

for sack in rucksacks:
    packing_error = False
    for item in sack[:len(sack) // 2]:
        
        if item in sack[len(sack) // 2:]:
            if packing_error:
                continue
            else:
                priority += alphabet.index(item) + 1
                packing_error = True
                


print(priority)
