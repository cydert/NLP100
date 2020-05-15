# -*- coding:utf8 -*-
import re

def rem_empha(st):
    m = re.search("(.*?)'{2,5}(.+?)'{2,5}(.*)",st)
    if m:
        st = "".join(m.groups())
        #print(st)
    return st

file_name = input()
dic = {}
with open(file_name) as f:
    text = f.read()

    m = re.search(r"\{\{基礎情報", text)
    text = text[m.end():]
    m = re.search(r"\n\}\}", text)
    text = text[:m.start()]
    
    for i in text.split("\n"):
        m = re.search(r"\|(.+?)=(.+)", i)
        if m:
            rem_st = rem_empha(m.group(2))
            dic[m.group(1)] = rem_st

    for k,v in dic.items():
        print(k + " : " + v)
