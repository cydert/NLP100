# -*- coding:utf8 -*-

file_name = input()
n = int(input())

lines = []
with open(file_name) as f:
    lines = [ i for i in f ]

size = len(lines)

one_size = len(lines) // n
remain = len(lines) % n

first_idx = 0
for i in range(0,n):
    last_idx = first_idx + one_size
    if( remain > 0 ):
        remain -= 1
        last_idx += 1
    with open("out_"+str(i) + ".txt", "w") as f:
        f.write( "".join(lines[first_idx:last_idx]) )

    first_idx = last_idx
        
