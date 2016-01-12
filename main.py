def PRINT():
    global zxc
    yu = 0
    for vb in zxc:
        op = 0
        for bn in zxc[yu]:
            print((zxc[yu])[op], end = ' ')
            op += 1
        print('\t')
        yu += 1

def A():
    if y >= 1:
        global y, c, f
        y -= 1
        (zxc[x])[y] = c
        (zxc[x])[y+1] = f
    else:
        print("you can't move in that direction")

def D():
    if y <= len(zxc[y]) - 1:
        global y, c, f
        y += 1
        (zxc[x])[y] = c
        (zxc[x])[y-1] = f
    else:
        print("you can't move in that direction")

def W():
    if x >= 1:
        global x, c, f
        x -= 1
        (zxc[x])[y] = c
        (zxc[x+1])[y] = f
    else:
        print("you can't move in that direction")

def S():
    if x <= len(zxc) - 1:
        global x, c, f
        x += 1
        (zxc[x])[y] = c
        (zxc[x-1])[y] = f
    else:
        print("you can't move in that direction")




f = input('field symbol is: ')
c = input('character symbol is: ')


hei = int(input('shir '))
wit = int(input('viss '))
WW = []
for xxx in range(wit):
    WW.append(f)
zxc = []
for xxx in range(hei):
    zxc.append(WW)


x = int(input('enter OX value: ')) - 1
y = int(input('enter OY value: ')) - 1

(zxc[x])[y] = c

while 1 == 1:
    dirc = int(input('enter direction: '))
    if dirc == -1:
        break
    elif dirc == 2:
        S()
    elif dirc == 8:
        W()
    elif dirc == 4:
        A()
    elif dirc == 6:
        D()
    
    PRINT()
        
input('thank you for playing')
