n=int(input())
l=[]
for i in range(n):
    c=['insert','print','remove','append','sort','pop','reverse']
    s=input().split()
    if s[0]==c[0]:
        l.insert(int(s[1]),int(s[2]))
    elif s[0]==c[1]:
        print(l)
    elif s[0]==c[2]:
        l.remove(int(s[1]))
    elif s[0]==c[3]:
        l.append(int(s[1]))
    elif s[0]==c[4]:
        l=sorted(l)
    elif s[0]==c[5]:
        l.pop(len(l)-1)
    elif s[0]==c[6]:
        l=list(reversed(l))
