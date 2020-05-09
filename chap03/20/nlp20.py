# -*- coding:utf8 -*-
import json

file_name = input()

with open(file_name) as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            print(data["text"])
            break
