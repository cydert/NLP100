# -*- conding:utf-8 -*-


def ngram(n, words=[]):
    ngram_set = set()
    for i in range(0, len(words)-n+1):
        ngram_set.add("".join( words[i:i+n] ))

    return ngram_set

x = input()
y = input()

x_bigram = ngram(2, list(x) )
y_bigram = ngram(2, list(y) )
print("x_bigram:",end="")
print(x_bigram)

print("y_bigram:",end="")
print(y_bigram)

print(x_bigram | y_bigram)
print(x_bigram & y_bigram)
print(x_bigram - y_bigram)
