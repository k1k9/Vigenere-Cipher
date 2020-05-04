from string import ascii_uppercase

''' Creating Caesar table 26X26'''
def caesar_table():
    table = []

    for i in range(len(ascii_uppercase)):
        table.append([]) # Create row

        for j in range(i, len(ascii_uppercase)):
            table[i].append(ascii_uppercase[j])
        
        for j in range(0, i):
            table[i].append(ascii_uppercase[j])
    return table