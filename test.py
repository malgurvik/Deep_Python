m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in m:
    print(*i)
m[0][1] = '+'
for i in m:
    print(*i)
# trans_m = list(map(list, zip(*m)))
# for i in trans_m:
#     print(*i)
