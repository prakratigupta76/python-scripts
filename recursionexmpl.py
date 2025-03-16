# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion Example Results:")
# tri_recursion(6)


# def printSumN(n):
#     if(n == 1):
#         return 1

#     return n + printSumN(n - 1)
# print(printSumN(5))


def sum_tail(n, sum=0):
    # Base case
    if n == 0:
        return sum
    # Tail recursive call with an accumulator
    else:
        return sum_tail(n-1, sum + n)
print(sum_tail(5))
# Output:
# 15
print("---------------------------------")

def printFactorial(n):

    if n == 1:
        result = 1
        return result
    else:
        result = n * printFactorial(n-1)
        # print(result)
    return result
print(printFactorial(5))

# Output:
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
    print(n)
    revprintNto1(n-1)
    
revprintNto1(5)

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

#Reverse a String
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))
#output: olleh

print("----------------------------------")

#Check If a Number is Palindrome
def is_pelindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_pelindrome(s[1:-1])

print(is_pelindrome("madam"))
print(is_pelindrome("hello"))
    
#output: 
# True
# False

print("----------------------------------")
#Print Even Numbers from 1 to N
def even_num(i, n):
    if i > n:
        return
    if i % 2 == 0:
        print(i, end= " ")
    even_num(i + 1, n)
even_num(1,10)

print()

def even_num(n):
    if n < 2:
        return
    even_num(n-2)
    print(n, end=" ")
even_num(10)
#output: 2 4 6 8 10
print()

print("--------------------------")

# Find the Sum of Digits of a Number

#method 1:
def sum_of_digit(n):
    if len(str(n))==1:
        return n
    return int(str(n)[0]) + sum_of_digit(int(str(n)[1:]))
print(sum_of_digit(1234))

print()

#method 2:
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)
print(sum_of_digits(1234))

print("--------------------------")

#Count the Number of Digits in a Number

# def count_digits(n):
#     return len(str(n))
# print(count_digits(9876))

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
print(count_digits(9876))
#Output: 4

print("--------------------------")
#Print Power of a Number (x^n)
def power_of_num(x,n):
    if n == 0:
        return 1
    return x * power_of_num(x, n-1)
print(power_of_num(50,2))
# Output: 2500

print("--------------------------")
def Great_common_div(x,n):
    if x == n:
        return x
    elif x < n:
        return Great_common_div(n,x) 
    return Great_common_div(n, x-n)
print(Great_common_div(24, 36))
#output: 12

