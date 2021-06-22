# 팩토리얼 _ 재귀함수 이용

var = int(input())

def factori(n):
    if n == 0:
        return 1

    if n > 0:
        return factori(int(n - 1)) * int(n)


print(factori(var))



