#입력수까지 덧셈
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
