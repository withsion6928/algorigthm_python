# A+B - 3 https://www.acmicpc.net/problem/11022 complete


case = int(input())
for i in range(case):
    a, b = map(int, input().split())
    c = a + b
    print("%d" % c)

