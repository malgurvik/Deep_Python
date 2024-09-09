from random import randint

# m = [[randint(1,10) for _ in range(3)] for _ in range(3)]
# print(m)


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
for i in m:
    print(*i)
for i in m2:
    print(*i)

res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(m)):
    for j in range(len(m[0])):
        res[i][j] = m[i][j] + m2[i][j]

print(res)
# for i in res:
#     print(*i)

# m[0][1] = '+'
# for i in m:
#     print(*i)
# trans_m = list(map(list, zip(*m)))
# for i in trans_m:
#     print(*i)
