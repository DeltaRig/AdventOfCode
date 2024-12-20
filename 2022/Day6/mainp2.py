# Daniela Rigoli Dezember 20 2024
# https://adventofcode.com/2022/day/6

def read_stacks_and_moves(file_name, size):
    with open(file_name, 'r') as f:
        marker = ""
        count = 0
        
        for line in f:
            while len(marker) < size:
                if(line[count] not in marker):
                    marker = marker + line[count]
                else:
                    marker = marker[marker.find(line[count])+1:]
                    marker = marker + line[count]
                count+=1
    print(marker)
    return count

file_name = 'input.txt'
result = read_stacks_and_moves(file_name, 14)
print("Caixas no topo das pilhas:", result)
