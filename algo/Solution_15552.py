#빠른 A+B https://www.acmicpc.net/problem/15552 complete
import sys

case = int(input())
for i in range(case):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
