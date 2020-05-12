# -*- coding:utf8 -*-
import re

file_name = input()
p = re.compile(r"^(=+)(.+?)=")   

with open(file_name) as f:
    for i in f:
        m = p.match(i)
        if m:
            level = len(m.group(1)) - 1
            sec_name = m.group(2)
            print("レベル:" + str(level), end="")
            print(" " + sec_name)
