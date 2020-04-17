# -*- coding:utf-8 -*-

st1 = input()
st2 = input()

if not len(st1) == len(st2):
    print("error: not same length")
else:
    for i in range(0,len(st1)):
        print(st1[i] + st2[i], end="")

print()
