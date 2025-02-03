# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion Example Results:")
# tri_recursion(6)


def printSumN(n):
    if(n == 1):
        result =1
        return result
    else:
        result = n + printSumN(n - 1)
        # print(result)
    return result
print(printSumN(5))

# Output:
# 3
# 6
# 10
# 15
print("---------------------------------")

def printFactorial(n):

    if n == 1:
        result = 1
        return result
    else:
        result = n * printFactorial(n-1)
        print(result)
    return result
printFactorial(5)

# Output:
# 2
# 6
# 24
# 120

print("---------------------------------")

def nthSequence(n):

    if n == 1:
        result = 1
        return result
    elif n == 2:
        result = 2
        return result
    else:
        result = nthSequence(n-1) + nthSequence(n-2)
    return result
print(nthSequence(7))
# Output:
# 3
# 5
# 3
# 8
# 3
# 5
# 13
# 3
# 5
# 3
# 8
# 21

print("---------------------------------")
# print name n times
def function(i, n):

    if i > n:
        return
    print ("Prakrati")
    function(i+1, n)
function(1, 5)

# Output:
# Prakrati
# Prakrati
# Prakrati
# Prakrati
# Prakrati
print("---------------------------------")


#print Linearly form 1 to n
# def print1toN(i,n):
#     if i > n:
#         return
#     print(i)
#     print1toN(i+1, n)
# print1toN(1, 5)

def print1toN(n):
    if n == 0:
        return 
    
    print1toN(n-1)
    print(n)

print1toN(5)
# Output:
# 1
# 2
# 3
# 4
# 5
print("---------------------------------")

#print form n to 1
def revprintNto1(n):
    if n == 0:
        return
    revprintNto1(n-1)
print(revprintNto1(5))

# def revprintNto1(i, n):
#     if i > n:
#         return
#     revprintNto1(i+1, n)
#     print(i)
# revprintNto1(1,5)

# def revprintNto1(i, n):
#     if i < 1:
#         return
#     print(i)
#     revprintNto1(i- 1, n)
# revprintNto1(5,5)

# output:
# 5
# 4
# 3
# 2
# 1
print("---------------------------------")

