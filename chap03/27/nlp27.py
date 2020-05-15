# -*- coding:utf8 -*-
import re

def rem_empha(st):
    m = re.search("(.*?)'{2,5}(.+?)'{2,5}(.*)",st)
    if m:
        st = "".join(m.groups())
        #print(st)
    return st

def rem_inter_link(st):
    while True:
        m = re.search(r"(.*)\[\[([^|]+?)\]\](.*)",st)
        if m:
            #print()
            #print(st)
            st = m.group(1) + m.group(2) + m.group(3)
            #print(st)
        else:
            break

    while True:
        m = re.search(r"(.*)\[\[[^|]+?\|([^|]+?)\]\](.*)",st)
        if m:
            #print()
            #print(st)
            st = m.group(1) + m.group(2) + m.group(3)
            #print(st)
        else:
            break
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
            rem_st = rem_inter_link(rem_st)
            dic[m.group(1)] = rem_st

    for k,v in dic.items():
        print(k + " : " + v)
