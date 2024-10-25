
type1 = 0
type2 = 0
tCase = int(input())
listt = []
for tCase in range(tCase):
    numTCase = int(input())
    numList = list(map(int, input().split()))
    for num in numList:
        if num < 2:
            type1 += 1
        else:
            type2 += 1 if num > 1 else 0
            type1 += num - 2 if num > 1 else 0
    listt.append(type1//2 + type2//2)
    type1 = 0
    type2 = 0
print(listt)