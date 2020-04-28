# -*- conding:utf8 -*-

file_name = input()
line_cnt = 0
with open(file_name) as f:
    for line in f:
        line_cnt += 1

print(line_cnt)
