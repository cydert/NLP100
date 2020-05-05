# -*- coding:utf8 -*-

file_name = input()

lines = []
tuple_list = []
with open(file_name) as f:
    for i, line in enumerate(f):
        lines.append(line)
        tuple_list.append( ( int(line.split()[2]), i) )

tuple_list.sort(key=lambda  x:x[0], reverse=True )

for t in tuple_list:
    print( lines[ t[1] ] ,end="")
