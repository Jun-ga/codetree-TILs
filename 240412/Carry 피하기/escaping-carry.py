def recur(start):
    global cnt
    #print(res)
    if res and not cal(res) :
        if len(res) - 1 > cnt:
            cnt = len(res)-1
        #print(cnt)
        return

    for i in range(start,N):
        res.append(num[i])
        #print('app',i,' ',res)
        recur(i+1)
        res.pop()
        #print('pop',i,' ',res)

def cal(res):
    prev_num = str(sum(res[:-1]))[::-1]
    next_num = str(res[-1])[::-1]
    min_len = min(len(prev_num), len(next_num))
    for i in range(min_len):
        if int(prev_num[i]) + int(next_num[i]) >= 10:
            return False
    return True
            
        
    

N = int(input())
num = []
res = []
cnt = 0
for _ in range(N):
    num.append(int(input()))
#cal(res)
recur(0)
print(cnt)