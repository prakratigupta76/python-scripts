#rivision
def printsqure(n):
    for i in range(n):
        print("*" * n)

printsqure(5)
print()
def printhollowSQR(n):
    for i in range(1,n+1):
        if i == 1 or i == n:
            print("*" * n) 
        else:
            print('*' + (" " * (n-2)) + "*")

printhollowSQR(5)
print()

def printLeftTri(n):
    for i in range(1, n+1):
        s = ''
        for j in range(i):
            s += '*'
        print(s)
        
printLeftTri(5)
print()

def printrevLeftTri(n):
    for i in range(n, 0, -1):
        s = ''
        for j in range(i):
            s += '*'
        print(s)
        
printrevLeftTri(5)
print()

def printRightTri(n):
    for i in range(1, n+1):
        s = ''
        for j in range(n-i):
            s += ' '
        for j in range(i):
            s += "*"
        print(s)
printRightTri(5)
print()

def printrevrRghtTri(n):
    for i in range(n, 0, -1):
        s = ''
        for j in range(n-i):
            s += ' ' 
        for j in range(i):
            s += "*"
        print(s)   

printrevrRghtTri(5)
print()

def printPyramid(n):
    for i in range(1, n+1):
        s = ''
        for j in range(n-i):
            s += ' '
        for j in range(i):
            if j is not i-1:
                s += "* "
            else:    
                s += "*"
        print(s)
printPyramid(5)
print()


def printpascalTri(n):
    for i in range(1, n+1):
        s = ''
        for j in range(n-i):
            s += ' '
        num = 1
        for j in range(1, i+1):
            s += str(num) + ' '
            num = num * (i-j) // (j)
        print(s)

printpascalTri(5)
print()

def printrevpascalTri(n):
    for i in range(n, 0, -1):
        s = ''
        for j in range(n-i):
            s += ' '
        num = 1
        for j in range(1, i+1):
            s += str(num) + ' '
            num = num * (i-j) // (j)
        print(s)

printrevpascalTri(5)
print()

def printnumpattern(n):
    for i in range(1, n+1):
        s = ''
        for j in range(i, i+n):
            s += str((j - 1) % n + 1)
        print(s)

printnumpattern(5)