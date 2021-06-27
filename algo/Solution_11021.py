# A+B - 7 https://www.acmicpc.net/problem/11021 complete


case = int(input())
for i in range(case):
    a, b = map(int, input().split())
    c = a + b
    print("Case #%d: %d" % (i+1, c))

