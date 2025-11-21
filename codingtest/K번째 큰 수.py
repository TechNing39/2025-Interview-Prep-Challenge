N,K=map(int,input().split())
result=[]
num=list(map(int,input().split()))
res=set()
for i in range(N):
    for j in range(i+1,N):
        for m in range(j+1,N):
            res.add(num[i]+num[j]+num[m])
           
result=list(res)
result.sort(reverse=True)
print(result)
print(result[K-1])


