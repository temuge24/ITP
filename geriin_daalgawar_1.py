#must
#bodlogo 1
"""
a = int(input("second oruul: "))
tsag = int(a/3600)
minute = int((a%3600)/60)
second = int(a%60)
print(tsag, "tsag", minute, "minute", second, "second")
"""
#bodlogo 2
"""
a = int(input("mungu oruul: "))
myanga_20 = int(a/20000)
myanga_10 = int(a%20000/10000)
myanga_5 = int(a%10000/5000)
myanga_1 = int(a%5000/1000)
print(myanga_20, "* 20000", myanga_10, "* 10000", myanga_5, "* 5000", myanga_1, "* 1000")
"""
#bodlogo 3
"""
a = int(input("3 оронтой тоо оруул: "))
zuut = a // 100
aravt = (a // 10) % 10
negj = a % 10
shine = negj * 100 + aravt * 10 + zuut
print(shine)
"""
#should
#bodlogo 1
"""
a = int(input("4 оронтой тоо оруул: "))
fist = a // 1000
second = (a % 1000) // 100
third = a % 100 // 10
last = a % 10
urjver = fist * fist + second * second + third *third + last * last
print(urjver)
"""
#bodlogo 2
"""
udur = int(input("udur: "))
tsag = int(input("tsag: "))
minute = int(input("minute: "))
second = int(input("second: "))
niit = udur * 24 * 60 * 60 + tsag * 60 * 60 + minute * 60 + second
print(niit)
"""
#bodlogo 3
"""
une = int(input("une: "))
hyamdral = int (input("hyamdral: "))
hasagdah = une // 100 *hyamdral
print(une - hasagdah)
"""
#challenge
#bodlogo 1
"""
a = input("6 orontoi too oruul: ")
ehnii_3 = int(a[:3])
last_3 = int(a[3:])
yalgawar = abs(ehnii_3 - last_3)
print(yalgawar)
"""
#bodlogo 2
"""
ehleh_tsag = int(input("ehleh tsag: "))
ehleh_min = int(input("ehleh min: "))
duusah_tsag = int(input("duusah tsag: "))
duusah_min = int(input("duusah min: "))
niit_min_ehleh = ehleh_tsag * 60 + ehleh_min
niit_min_duusah = duusah_tsag * 60 + duusah_min
zoruu_minut = niit_min_duusah - niit_min_ehleh
print(zoruu_minut)
"""
#bodlogo 3
"""
a = input("5 orontoi too oruul: ")
urjver = int(a[::2]) * int(a[1::2])
print(urjver)
"""
