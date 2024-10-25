


tCase = int(input()) 
for tCase in range(tCase):
    sumCurr = 0
    sumNeed = 0
    gemLv = int(input())
    gemCurr = input().split()
    gemNeed = input().split()

    for i in range(gemLv-1, 0, -1):
        sumCurr = (sumCurr + int(gemCurr[i]))*2
        sumNeed = (sumNeed + int(gemNeed[i]))*2
    
    sumCurr += int(gemCurr[0])
    sumNeed += int(gemNeed[0])
    if sumCurr >= sumNeed:
        print("YES")
    else:
        print("NO")
