d={}
t=0
for i in range(int(input())):
    a=input().split(' ')
    d[a[0]]=a[1:]
for i in d[input()]:
    t=t+float(i)
p=float(t/3)
print('%.2f'%p)
