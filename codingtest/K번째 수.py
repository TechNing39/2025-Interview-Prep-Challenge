T=int(input())
for i in range(T):  
    N,s,e,k=map(int,input().split())
    num=[]
    num2=[]

    for i in range(N):
        num.append(int(input()))

    for x in range(s-1,e):
        num2.append(num[x])
    num2.sort()

    print(num2[k-1])
