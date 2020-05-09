# -*- coding:utf8 -*-

file_c1 = input()
file_c2 = input()
out_file = input()

list_c1 = []
list_c2 = []
with open(file_c1) as f:
    list_c1 = [ i.strip() for i in f ]
with open(file_c2) as f:
    list_c2 = [ i.strip() for i in f ]

with open(out_file, mode="w") as f:
    for i in range(0,len(list_c1)):
        f.write( list_c1[i] + "\t" + list_c2[i] + "\n" )

