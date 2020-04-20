# -*- coding:utf-8 -*-

st = input()
st = st.replace(",","")
st = st.replace(".","")
words = st.split()
word_len_list = [ len(word) for word in words ]
print(word_len_list)

