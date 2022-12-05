import re

with open("input.txt", "r") as f:  
    section_list = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", f.read())
    section_list = [[int(x) for x in pair] for pair in section_list]

contained_pairs = 0

for pair in section_list:
    if pair[0] >= pair[2] and pair[1] <= pair[3]:
        contained_pairs += 1
    elif pair[2] >= pair[0] and pair[3] <= pair[1]:
        contained_pairs += 1     


#--- PART 2 ---

overlaping_pairs = 0

for sect in section_list:
    does_it_overlap = False
    seq = {section for section in range(sect[0], sect[1] + 1)}
    seq2 = {section for section in range(sect[2], sect[3] + 1)}

    if seq.intersection(seq2):
        overlaping_pairs += 1    

print(overlaping_pairs)            
