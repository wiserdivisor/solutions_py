n=int(input())
l=list(map(int,input().split()))[:n]
m=max(l)
while m==max(l):l.remove(max(l))
print(max(l))
