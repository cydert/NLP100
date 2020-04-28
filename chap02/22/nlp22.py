# -*- coding:utf8 -*-

file_name = input()
out_name1 = input()
out_name2 = input()

f1 = open(out_name1,mode="w")
f2 = open(out_name2,mode="w")

c1_lis = []
c2_lis = []
with open(file_name) as f:
    for line in f:
        cols = line.split()
        c1_lis.append(cols[0])
        c2_lis.append(cols[1])

f1.write("\n".join(c1_lis))
f2.write("\n".join(c2_lis))
f1.close()
f2.close()
