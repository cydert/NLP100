# -*- coding:utf8 -*-

file_name = input()
one_lines = []

with open(file_name) as f:
    one_lines = [ i.split()[0] for i in f ]

uni_set = set(one_lines)
uni_set = sorted(uni_set)
for i in uni_set:
    print(i)
