def recur(start):
    global cnt
    if sum(res) > 10 and len(res) - 1 > cnt :
        cnt = len(res)-1
        return

    for i in range(start,N):
        res.append(num[i])
        #print('app',res)
        recur(i+1)
        res.pop()
        #print('pop',res)



N = int(input())
num = []
res = []
cnt = 0
for _ in range(N):
    num.append(int(input()[-1]))

recur(0)
print(cnt)