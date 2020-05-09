# -*- coding:utf8 -*-

file_name = input()
dic = {}

with open(file_name) as f:
    for i in f:
        c1 = i.split()[0]
        dic[c1] = dic.get(c1, 0) + 1

dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

for i in dic:
    print(i[0] + " " + str(i[1]))


