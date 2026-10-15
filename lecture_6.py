# #bodlogo 1
# def double(x):
#     print(x * 2)
# double(5)
# double(12)
# #bodlogo 2
# def mendchilge(x):
#     print("sain baina uu", x)
# mendchilge("anu")
# #bodlogo 3
# def area(a, b):
#     print("talbai: ", a*b)
# area(4, 5)
# #bodlogo 4
# def check_even(x):
#     if(x%2==0):
#         print("tegsh")
#     else:
#         print("sondgoi")
# check_even(5)
# #bodlogo 5
# def find_max(a, b):
#     if(a>b):
#         print("max: ", a)
#     else:
#         print("max: ", b)
# find_max(4, 5)
# #bodlogo 6
# def sum_numbers(x):
#     sum =0
#     for i in range(x):
#         sum +=i
#     print(sum)
# sum_numbers(5)
# #bodlogo 7
# def digit_sum(x):
#     i =0
#     sum =0 
#     while x>0:
#         a = x%10
#         x = x//10
#         sum = sum+a
#     print(sum)
# digit_sum(1234)
#bodlogo 8
def is_prime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True
if is_prime(23):
    print("anhnii too")
else:
    print("anhnii too bish")
#bodlogo 9

def print_even(a, b):
    a =[]
    for i in range(a, b):
        if i%2==0:
            a.append(i)
        else:
            continue
    print(a)
print_even(3, 12)