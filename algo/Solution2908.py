
#상수 https://www.acmicpc.net/problem/2908    complelte
a, b = map(int,input().split())

# print(''.join(reversed(str(a))))
aa = ''.join(reversed(str(a)))
bb = ''.join(reversed(str(b)))

if aa > bb:
    print(aa)
else:
    print(bb)