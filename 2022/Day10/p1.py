from pathlib import Path
file = 'input.txt'
lines = Path(file).read_text().splitlines()

x = 1
c = 0
m = 0
s = 0

def op():
    global c
    global m
    global s
    global x
    c += 1 
    if(c == 20 + (m * 40)):
        s += c * x
        print("ciclos: ", c, " / X: ", x, )
        print("/ S: ", c * x, " / m ", m, " I ", i)
        print()
        m +=1
    

for instruction in lines:
    if instruction == 'noop':
        op()
        continue
    # addx V
    i = int(instruction.split()[1])
    if(i == -9):
        print("AQUI")
    # r = i if i > 0 else 1
    for v in range(2):
        op()
    x += i

print("ciclos: ", c, " / X: ", x, " / m ", m)
print("Strangths ",  s)

    
"""
c   x
1 - 1
aadx 3
2
3
4 - 4
addx -5
5 - -1
"""

"""
c  x   m
180 16
addx -9
182 7
addx 18
184 25
addx 1
186 25
addx 2
188 27
noop
189
noop
190
addx 9
192 36
noop
193
noop
194
noop
195
addx -1
197 35
addx 2
199 37
addx -37
201 0
addx 1
203 1
addx 3
205 4
noop
206
addx 15
208 19
addx -21
210 -2
addx 22
212 20
addx -6
214 14
addx 1
216 15
noop
217
addx 2
219 17
addx 1
220 XXXX
"""
