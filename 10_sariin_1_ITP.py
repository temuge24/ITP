import math
#bodlogo 1
"""
number = int(input("3 oronotoi too oruul: "))
a = int(number/100)
b = int(number%100/10)
c = int(number%10)
urjver = a*c*b
print(f"urjver: {urjver}")
"""
#BODLOGO 2
"""
number = int(input("4 oronotoi too oruul: "))
a = int(number/1000)
b = int(number%1000/100)
d = int(number%100/10)
c = int(number%10)
urjver = a*c*b*d
print(f"urjver: {urjver}")
"""
#bodlogo 3
"""
a = int(input("a taliig ug: "))
b = int(input("b taliig ug"))
ab = a*b
print(f"talibai n {ab}")
"""
#bodlogo 4
"""
a = int(input("1 r too:  "))
b = int(input("2 r too: "))
arif= (a + b)/2
gio = math.sqrt(a*b)
"""
#bodlog 5
"""
n = int(input("too oruul : "))
if n<0 :
    print("surug too")
else:
    print("eyreg too")
    """
#bodlogo 6
"""
n = int(input("too oruul : "))
if n%2==0 :
    print("tegsh too")
else:
    print("sondgoi too")
    """
#bodlogo 7
"""
n = int(input("2 too oruul : "))
a =n/10
b = n%10
if a==b:
    print("palindrome mun")
else:
    print("palindrome bish")
"""
#bodlogo 8
"""
number = int(input("3 oronotoi too oruul: "))
a = int(number/100)
b = int(number%100/10)
c = int(number%10)
if a>b and a>c :
    max = a
elif b>a and b>c:
    max = b
else:
    max = c
print(f"max: {max}")
"""
#bodlogo 9
"""
a = int(input("1 r too:  "))
b = int(input("2 r too: "))
arif= (a + b)/2
if arif%2==0:
    print("arifmetic n tegsh too")
else:
    print("arifmetic n sondgoi too")
"""
#bodlogo 10
"""
number = int(input("3 oronotoi too oruul: "))
a = int(number/100)
b = int(number%100/10)
c = int(number%10)
if a==c:
    print("palindrome too mun")
else:
    print("bish")
if b%2==0:
print("sondgoi bish")
else:
print("sondgoi")
"""
#      should 1
#bodlogo 1
# x =[]
# y=[]
# for i in range(3):
#     a= int(input(f"X {i+1} r too: "))
#     x.append(a)
#     b = int(input(f"Y {i+1} r too: "))
#     y.append(b)
# S = (x[0]*(y[1]-y[2]) + x[1]*(y[2]-y[0]) + x[2]*(y[0] - y[1]))/2
# print("talbai n :", abs(S))
#      should 2
# a = []
# for i in range(3):
#     n = int(input(f"{i+1} r toogoo oruul: "))
#     a.append(n)
# result = sorted(a[0], a[1], a[2])
# print(result)
#should 3
# a = []
# for i in range(4):
#     n = int(input(f"{i+1} r toogoo oruul: "))
#     a.append(n)
# result = min(a[0], a[1], a[2], a[3])
# print(result)
#should 4
number = int(input("4 oronotoi too oruul: "))
a = int(number/1000)
b = int(number%1000/100)
d = int(number%100/10)
c = int(number%10)
if number%a==0 or number%b==0 or number%c==0 or number:
    print