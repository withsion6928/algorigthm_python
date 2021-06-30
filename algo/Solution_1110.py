# 더하기 사이클 https://www.acmicpc.net/problem/1110 complete

origin = input()
tmp1 = origin
idx = 0
while True:
    if int(tmp1) < 10:
        tmp1 = '0' + str(tmp1)

    a = int(tmp1[0]) + int(tmp1[-1])

    if a < 10:
        a = '0' + str(a)

    tmp2 = tmp1[-1] + str(a)[-1]

    tmp1 = tmp2
    idx += 1

    if tmp2 == origin or tmp2 == '0' + origin:
        break

print(idx)
