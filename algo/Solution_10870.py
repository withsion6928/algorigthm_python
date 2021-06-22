#피보나치수 https://www.acmicpc.net/problem/10870 complete

var = int(input())


def fibonachi(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


print(fibonachi(var))
