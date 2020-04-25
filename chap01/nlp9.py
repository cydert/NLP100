#-*- coding:utf8 -*-
import random

st = input()

words = st.split()

shuf_word = ""
for word in words:
    if len(word) > 4:
        part_word = word[1:len(word)-1]
        part_shuf_word = "".join( random.sample(part_word, len(part_word) ))
        word = word[0] + part_shuf_word + word[len(word)-1]

    shuf_word += word + " "

print(shuf_word)
    
