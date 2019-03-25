import math

p = 522590389
g = 2164

a_result = 492973999
b_result = 8199534 

i = 0
while True:
    res = (g**i)%p
    if res == a_result:
        print("a: {}".format(i))
    if res == b_result:
        print("b: {}".format(i))
    if (i%10000 == 0):
        print(i)
    i += 1
