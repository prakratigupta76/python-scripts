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
        print(result)
    return result
printSumN(5)
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

print("---------------------------------")

def printNthSequence(n):

    if n == 1:
        result = 1
        return result
    elif n == 2:
        result = 2
        return result
    else:
        result = printNthSequence(n-1) + printNthSequence(n-2)
        print(result)
    return result
printNthSequence(7)