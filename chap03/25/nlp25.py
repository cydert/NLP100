# -*- coding:utf8 -*-
import re

file_name = input()
dic = {}
with open(file_name) as f:
    text = f.read()

    m = re.search(r"\{\{基礎情報", text)
    text = text[m.end():]
    m = re.search(r"\}\}", text)
    text = text[:m.start()]
    
    for i in text.split("\n"):
        m = re.search(r"\|(.+?)=(.+)", i)
        if m:
            dic[m.group(1)] = m.group(2)

    print(dic)
