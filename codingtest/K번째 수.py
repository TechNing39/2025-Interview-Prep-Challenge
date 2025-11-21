T=int(input())
for i in range(T):  
    N,s,e,k=map(int,input().split())

    num=list(map(int,input().split()))

    num2=num[s-1:e]
    num2.sort()

    print("#%d %d" % (i + 1, num2[k - 1]))
