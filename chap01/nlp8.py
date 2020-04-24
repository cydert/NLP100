# -*- condig:utf-8 -*-

def cipher(st):
    ans = ""
    for s in st:
        ci = s
        if s.islower() == True:
            ans += chr( 219 - ord(s) )

    return ans

st = input()
cip_st = cipher(st)
dec_st = cipher( cip_st )

print("暗号化:%s" % cip_st)
print("復号化:%s" % dec_st)
