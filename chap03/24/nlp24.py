# -*- coding:utf8 -*-
import re
file_name = input()

p = re.compile(r"\[\[ファイル:(.*?)\|")
with open(file_name) as f:
    for i in f:
        m = p.match(i)
        if m:
            print(m.group(1))
