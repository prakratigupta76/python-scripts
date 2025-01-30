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

# output:
#     1
#    2_2
#   3_3_3
#  4_4_4_4
# 5_5_5_5_5

print("....................")

def printNumIncreasing(n):
    for i in range (1,n+1):
        s = ''
        for j in range(1, i+1):
            s += str(j)
        print(s)

printNumIncreasing(5)

# Output:
# 1
# 12
# 123
# 1234
# 12345

print("....................")

def printNumIncreasingRev(n):
    for i in range (1,n+1):
        s = ''
        for j in range(1, n-i+2):
            s += str(j)
        print(s)

printNumIncreasingRev(5)

# Output:
# 12345
# 1234
# 123
# 12
# 1

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

# Output:
# 1
# 01
# 101
# 0101
# 10101

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

# Output:
# 1
# 01
# 101
# 0101
# 10101

def printZero_onetriangle3(n):
    start = ''
    for i in range (1,n+1):
        
        if i % 2 ==  0:
            start = '0' + start
        else:
            start = '1' + start
        print(start)

printZero_onetriangle3(5)

# Output:
# 1
# 01
# 101
# 0101
# 10101

print("....................")

def printPalindromeTri(n):
    s = '1'
    for i in range(2, n+1):
        space = ''
    
        for j in range(n-i):
            space += " "
        
        print(space + s)
        s = str(i) + s + str(i)

printPalindromeTri(5)

# Output:
#    1
#   212
#  32123
# 4321234

print("....................")

def printRohmbus(n):
    for i in range(n, 0, -1):
        s = ''

        for j in range(n-i+1):
            s += " "
        for j in range(n-1):
            s += "*"

        print(s)

printRohmbus(5)

# Output:
#  *****
#   *****
#    *****
#     *****
#      *****

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
    

        print(s)
    for i in range(n-1, 0, -1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(i):
            s += "*"
            if j != i-1:
                s+=' '
    

        print(s)
printDiamond(5)
# output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


print("----------------------------")

def printRightHalf(n):
    for i in range(1,n+1):
        s = ''
        for j in range(i):
            s+= "*"

        print(s)
printRightHalf(5)
# Output:
# *
# **
# ***
# ****
# *****

print("----------------------------")


def printRevRightHalf(n):
    for i in range(1,n+1):
        s = ''
        for j in range(n-i+1):
            s+= "*"

        print(s)
printRevRightHalf(5)
# Output:
# *****
# ****
# ***
# **
# *

print("----------------------------")


def printLeftHalfPyramid(n):
    
    for i in range(1,n+1):
        s = ""
        for j in range(n-i+1):
            s+= " "
        for j in range(i):
            s+= "*"

        print(s)

printLeftHalfPyramid(5)
# Output:
#      *
#     **
#    ***
#   ****
#  *****

print("----------------------------")

def printRevLeftHalfPyramid(n):
    
    for i in range(1,n+1):
        s = ""
        for j in range(i):
            s+= " "
        for j in range(n-i+1):
            s+= "*"

        print(s)

printRevLeftHalfPyramid(5)
# Output:
#  *****
#   ****
#    ***
#     **
#      *

print("----------------------------")

def printKpattern(n):
    
    for i in range(1,n+1):
        s = ""
        for j in range(n-i+1):
            s+= "*"
        
        print(s)
    for i in range(2,n+1):
        s = ""
        for j in range(i):
            s+= "*"
    
        print(s)
printKpattern(5)
# Output:
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****

print("----------------------------")

# def printButtrflyStar(n):
#     for i in range(1,n-i+1):
#         s = ''
#         for j in range(i):
#             s+= "*"

#         print(s)

#     for i in range(2,n-i+1):
#         s = ''
#         for j in range(n-i+1):
#             s+= "*"

#         print(s)


#     # for i in range(1,n+1):
#     #     s = ''
#     #     for j in range(n-i+1):
#     #         s+= " "
#     #     for j in range(i):
#     #         s+= "*"

#     #     print(s)

#     # for i in range(2,n+1):
#     #     s = ''
#     #     for j in range(i):
#     #         s+= " "
#     #     for j in range(n-i+1):
#     #         s+= "*"

#     #     print(s)

# printButtrflyStar(5)
# Output:
# 

print("----------------------------")

def printTriStar(n):

    for i in range(1,n+1):
        s = ''
        for j in range(n-i+1):
            s += " "
        for j in range(i):
            s+="*"
            if j != i:
                s += " "
        print(s)
printTriStar(5)
# Output:
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *


print("----------------------------")

def printRevNumStar(n):

    for i in range(n, 0, -1):
        s = ''
        for j in range(n-i, 0, -1): 
            s+=" "
        for j in range(n-i+1, n+1):
            s+= str(j)
            s+= " "
        print(s)
printRevNumStar(5)
# Output: 
# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5

print("----------------------------")

import math
def printButtrflyStar(n):
    n = math.ceil(n/2)
    for i in range(1,n+1):
        s = ''
        for j in range(i):
            if j != n-1:
                s += "*"
        for j in range(n-i-1) :
            s+=" "   
        
        for j in range(n-i) :
            s+=" "
        for j in range(i):
            s+="*"
        print(s)


    for i in range(2,n+1) :
        s = '' 
        for j in range(n-i+1):
            s+="*"
        for j in range(i-2):
            s += " "
        
        for j in range(i-1):
            s += " "
        for j in range(n-i+1):
            s+="*"
        print(s)

printButtrflyStar(5)
# Output: 
# *   *
# ** **
# *****
# ** **
# *   *
print("----------------------------")

def printHollowTri(n):
    for i in range(1, n+1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(1, i+1):
            if i == n:
                s += "* "
                
            else:
                if j == 1 or j == i:
                    s+="* "
                else:
                    s+="  "
        print(s.rstrip())

printHollowTri(5)
# Output:
#     *
#    * *
#   *   *
#  *     *
# * * * * *

print("----------------------------")

def printMirrorTri(n):
    for i in range(n,0,-1):
        s = ''
        for j in range(n-i, 0, -1): 
            s+=" "
        for j in range(n-i+1, n+1):
            s+= str(j)
            s+= " "
        print(s)
    for i in range(2,n+1):
        s = ''
        for j in range(n-i, 0, -1): 
            s+=" "
        for j in range(n-i+1, n+1):
            s+= str(j)
            s+= " "
    
        print(s)
printMirrorTri(5)
# Output:
# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5 
#    4 5
#   3 4 5
#  2 3 4 5
# 1 2 3 4 5
print("----------------------------")

def printRevHollowTri(n):
    for i in range(n,0,-1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(1, i+1):
            if i == n or j == 1 or j == i:
                    s+="* "
            else:
                s+="  "
        print(s.rstrip())
printRevHollowTri(5)
# def printRevHollowTri(n):
#     for i in range(n, 0, -1):
#         s = ' ' * (n - i)  # Add leading spaces

#         for j in range(1, i + 1):  # Print '*' and spaces
#             if i == n or j == 1 or j == i:
#                 s += "* "
#             else:
#                 s += "  "  # Two spaces to maintain alignment

#         print(s.rstrip())  # Remove extra spaces at the end

# printRevHollowTri(5)
# Output:
# * * * * *
#  *     *
#   *   *
#    * *
#     *
print("----------------------------")

def printHollowDiamond(n):
    for i in range(1,n+1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(1, i+1):
            if j == 1 or j == i:
                    s+="* "
            else:
                s+="  "
        print(s.rstrip())

    for i in range(n-1,0,-1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(1, i+1):
            if j == 1 or j == i:
                    s+="* "
            else:
                s+="  "
        print(s.rstrip())
printHollowDiamond(5)
# output:
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
print("----------------------------")

def printHollowHourglass(n):
    for i in range(n,1,-1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(1, i+1):
            if i == n or j == 1 or j == i:
                    s+="* "
            else:
                s+="  "
        print(s.rstrip())

    for i in range(1,n+1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(1, i+1):
            if i == n or j == 1 or j == i:
                    s+="* "
            else:
                s+="  "
        print(s.rstrip())
printHollowHourglass(5)
# output:
# * * * * *
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# * * * * *
print("----------------------------")

def printPascaltri(n):
    for i in range(1,n+1):
        s = ''
        for j in range(n-i):
            s += " "
        for j in range(1, i+1):
            if j == 1 or j == i:
                    s+="1 "
            else:
                s+=str(i-1)
                s+=" "
        print(s)
printPascaltri(5)
# Output:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 4 4 1
print("----------------------------")
def printRightPascal(n):
    n = math.ceil(n/2)
    for i in range(1,n+1):
        s = ''
        for j in range(i):
            s+= "*"

        print(s)
    for i in range(2,n+1):
        s = ''
        for j in range(n-i+1):
            s+= "*"

        print(s)
printRightPascal(5)
# output:
# *
# **
# ***
# **
# *
print("----------------------------")