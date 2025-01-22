def printSqrHollow(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("*"*n)
        else:
            print("*" + (" " * (n-2)) + "*")

printSqrHollow(5)

# output:
# *****
# *   *
# *   *
# *   *
# *****

print("....................")

def printSqrFill(n):
    for i in range(n):
        print("*"*n)

printSqrFill(5)
# output:
# *****
# *****
# *****
# *****
# *****

print("....................")

def printLeftHalfPyramid(n):
    j=1
    for i in range(n):
        print(" "*(n-i) + "*"*j)
        j+=1

printLeftHalfPyramid(5)
# output:
#      *
#     **
#    ***
#   ****
#  *****

print("....................")

def printNumTringular(n):
    for i in range(1,n+1):
        s = ''
        for j in range(n-i):
            s+=" "
        for j in range(i):
            s+=str(i)
            if j != i-1:
                s+='_'
        print(s)
printNumTringular(5)

print("....................")

def printNumIncreasing(n):
    for i in range (1,n+1):
        s = ''
        for j in range(1, i+1):
            s += str(j)
        print(s)

printNumIncreasing(5)

print("....................")

def printNumIncreasingRev(n):
    for i in range (1,n+1):
        s = ''
        for j in range(1, n-i+2):
            s += str(j)
        print(s)

printNumIncreasingRev(5)

print("....................")


def printZero_onetriangle(n):
    for i in range (1,n+1):
        s = ''
        for j in range(1,i+1):
            if (j % 2 == 0 and i %2 == 0) or (j % 2 == 1 and i %2 == 1):
                s += '1'
            else:
                s += '0'
            
        
        print(s)

printZero_onetriangle(5)

def printZero_onetriangle2(n):
    start = 1
    for i in range (1,n+1):
        tempstart = start
        s = ''
        for j in range(1,i+1):
            s+= str(tempstart)
            if tempstart == 1:
                tempstart = 0
            else:
                tempstart = 1
            
        if start == 1:
            start = 0
        else:
            start = 1
        print(s)

printZero_onetriangle2(5)

def printZero_onetriangle3(n):
    start = ''
    for i in range (1,n+1):
        
        if i % 2 ==  0:
            start = '0' + start
        else:
            start = '1' + start
        print(start)

printZero_onetriangle3(5)

print("....................")

# def printPalindromeTri(n):
#     for i in range(1, n+1):
#         s = ''
#         k = "1"
#         for j in range(n-i):
#             s += " "
#         for j in range(i):
#             s += k
#             k += str(i)
        
#         print(s)

# printPalindromeTri(5)

print("....................")

def printRohmbus(n):
    for i in range(n, 0, -1):
        s = ''

        for j in range(n-i+1):
            s += " "
        for j in range(n):
            s += "*"

        print(s)

printRohmbus(5)

print("....................")

def printDiamond(n):
    for i in range(1, n+1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(i):
            s += "*"
            if j != i-1:
                s+=' '
    for i in range(1, n):
        for j in range(i, 0, -1):
            s += "*"
            if j != i-1:
                s+=' '

        for j in range(n-i):
            s += " "
        print(s)

printDiamond(5)