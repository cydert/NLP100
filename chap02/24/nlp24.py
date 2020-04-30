# -*- coding:utf8 -*-

n = int(input())
file_name = input()

with open(file_name) as f:
    for i in range(0,n):
        print(f.readline(),end="")
