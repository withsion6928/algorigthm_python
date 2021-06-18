#최대값

listArr = []

for i in range(9):
    listArr.append(int((input().rstrip())))


print(max(listArr))
print(listArr.index(max(listArr))+1)
