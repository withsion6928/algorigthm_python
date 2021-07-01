# 단어공부 https://www.acmicpc.net/problem/1157 complete
word = input()

word = word.upper()

wordList = list(set(word))
cnt = []

for i in wordList:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(wordList[cnt.index(max(cnt))])






