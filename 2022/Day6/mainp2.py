# Daniela Rigoli Dezember 20 2024
# https://adventofcode.com/2022/day/6

def findMarker(file, size):
    with open(file, 'r') as f:
        marker = ""
        count = 0
        
        for line in f:
            while len(marker) < size:
                find = marker.find(line[count])
                if(find == -1):
                    marker = marker + line[count]
                else:
                    marker = marker[find+1:]
                    marker = marker + line[count]
                count+=1
    print(marker)
    return count

file = 'input.txt'
result = findMarker(file, 14)
print("Caixas no topo das pilhas:", result)
