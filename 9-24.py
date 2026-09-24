#bodlogo 1
"""
a = int(input())
if a%2==0:
    print("tegsh")
else:
    print("sondgoi")
"""
#bodlogo 2
"""
a= int(input())
if a>90 and a<101:
    print("A")
elif a>80 and a<90:
    print("B")
elif a>70 and a<80:
    print("C")
elif a>60 and a<70:
    print("D")
elif a>=0 and a<60:
    print("F")
else :
    print("onoo buruu baina")
"""
#bodlogo 3
"""
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    max = a
elif b>a and b>c:
    max =b
else :
    max=c
print("max n:", max)
"""
#bodlogo 4
"""
for i in range(2, 20):
    if i %2 ==0:
        print(i)
    else :
        continue
"""
#bodlogo 5
"""
a = int(input())
niilber=0
for i in range(2, a+1):
    if i %2 ==0:
        niilber+=i
    else :
        continue
print("niilber n:", niilber)
"""
#bodlogo 6
b ="Nest2026"
a = input()
for i in range (3):
    if a == b:
        t=1
    else :
        print("buruu") 
        t=0
if t==1:
    print("amjilttai nevterlee") 
    break
else:
    print("oroldlogo duuslaa")