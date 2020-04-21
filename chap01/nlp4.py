# -*- coding:utf-8 -*-

st = input()
word_list = st.split()
dic={}

index_list = [1,5,6,7,8,9,15,16,19] #get one char index

for i in range(0, len(word_list)):
    if ( (not len(index_list) == 0) and index_list[0] == i+1 ):
        #one char
        del index_list[0]
        #print(word_list[i][0])
        dic[ word_list[i][0] ] = i+1
    else:
        #print(word_list[i][:2])
        dic[ word_list[i][:2] ] = i+1

print(dic)
