# -*- coding:utf-8 -*-

def ngram(n, words=[]):
    i = 0

    while i+(n-1) < len(words):
        #print(words[i:i+n])
        print("".join( words[i:i+n] ) )
        i+=1

print("ngramのnの値を入力してください")
n = int(input())
print("文字を入力してください")
st = input()
words = st.split()
chars = list(st)
chars = [c for c in chars if c != " "]

ngram(n, words)
print()
ngram(n, chars)

