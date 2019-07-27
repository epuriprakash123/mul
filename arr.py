n=int(input())
l=list(map(int,input().split()))
m=1
for i in range(n):
	m=m*l[i]
k=[]	
for i in range(n):
	j=m//l[i]
	k.append(j)
print(*k)	
