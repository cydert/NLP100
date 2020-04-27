# -*- coding:utf8 -*-

file_name = input()
with open(file_name) as f:
    lines = [ line.strip().replace("\t"," ") for line in f ]

for line in lines:
    print(line)
