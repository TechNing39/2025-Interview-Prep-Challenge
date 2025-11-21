N=int(input())
score=list(map(int,input().split()))
sum=0
for i in range(N):
    sum=sum+score[i]
avg=round(sum/N)

min_diff = float('inf')
res=0

for idx,x in enumerate(score):
    tmp=abs(x-avg)

    if tmp<min_diff:
        min_diff=tmp
        res=idx+1
        res_score=x

    elif tmp==min_diff:
        if x>res_score:
            res_score=x
            res=idx+1

print(avg,res)



