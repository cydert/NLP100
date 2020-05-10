# -*- coding:utf8 -*-
import re

file_name = input()

p = re.compile("\[\[Category:.+\]\]")
with open(file_name) as f:
    for i in f:
        if p.match(i) != None:
            print(i, end="")
        
