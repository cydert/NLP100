# -*- coding:utf8 -*-

file_name = input()
n = int(input()) #last print n
lines = []

with open(file_name) as f:
    lines = [ i.rstrip() for i in f ]

for i in range( len(lines) - n, len(lines) ):
    print(lines[i])
