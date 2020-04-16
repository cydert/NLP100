# -*- coding:utf-8 -*-
#reverce program
import queue

print("input")
st = input()

MODE=1

if MODE == 0:
    print(st[::-1]) #slice
elif MODE == 1:
    stack = queue.LifoQueue()
    for c in st:
        stack.put(c)
    
    while not stack.empty():
        print(stack.get(),end="")
    print()


