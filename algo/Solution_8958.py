# OX퀴즈 https://www.acmicpc.net/problem/8958 complete

n = int(input())


def getSumGrade(inputList):
    resultList = []
    for i in range(len(inputList)):
        if (inputList[i]) == 'O' and i == 0:
            resultList.append(1)
        elif i > 0 and resultList[-1] != 0 and inputList[i] == 'O':
            resultList.append((int(resultList[-1]) + 1))
        elif i > 0 and inputList[i] == 'O':
            resultList.append(1)
        else:
            resultList.append(0)

    sumR = 0
    sumR = sum(resultList)

    return sumR


while True:
    try:
        arr = list(input())
        print(getSumGrade(arr))
    except EOFError:
        break
