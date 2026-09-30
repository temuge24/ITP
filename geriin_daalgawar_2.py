#must 1
"""
first_name = "temuge"
age = 15
height = 1.77
is_student = "yes"
print(type(first_name))
print(type(age))
print(type(height))
print(type(is_student))
"""
#should 1
"""
x = 25
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))
"""
#challenge 1
"""
suragchiin_ner = "Temuulen"
angi = 11
average_score = 92.5
tulbur_tulsun = "true"
hicheeluud = "Python, Java, Math"
print(suragchiin_ner, type(suragchiin_ner))
print(angi, type(angi))
print(average_score, type(average_score))
print(tulbur_tulsun, type(tulbur_tulsun))
print(hicheeluud, type(hicheeluud))
"""
#must 2
"""
text = "Programming"
print(text[0])
print(text[3])
print(text[6])
print(text[-1])
print(len(text))
"""
#should 2 
"angi deer hiigeed uzuultsen bsan shu bagsha"
#challenge 2
"angi deer hiigeed uzuultsen bsan shu bagsha"
#must 3
"""
a = int(input())
if a%2==0:
    print("tegsh")
else:
    print("sondgoi")
"""
#should 3
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
#challenge 3
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
#must 4
"""
for i in range(2, 20):
    if i %2 ==0:
        print(i)
    else :
        continue
"""
#should 4
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
#challenge 4
"""
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
    """
# bonus
"""
onoonuud = []
niilber = 0
ner = input("ner : ")
for i in range(3):
    onoo = int(input(f"{i+1}-r hichelling onoo"))
    onoonuud.append(onoo)
    niilber += onoo
print(ner.upper())
print(niilber)
dundaj = niilber/3
print(dundaj)
if dundaj>=80:
    is_pass = "amjilttai"
else:
    is_pass = "saijruulah shardlagatai"
print(f"{is_pass}")
"""