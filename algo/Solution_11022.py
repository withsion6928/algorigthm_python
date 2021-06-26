# A+B - 8 https://www.acmicpc.net/problem/11022 complete


case = int(input())
for i in range(case):
    a, b = map(int, input().split())
    c = a + b
    print("Case #%d: %d + %d = %d" % (i+1, a,b, c))

