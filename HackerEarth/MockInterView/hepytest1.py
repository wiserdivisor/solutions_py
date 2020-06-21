import re

def findmin(s):
    d = dict()
    s = ''.join(sorted(s))

    sub = [m.group(0)for m in re.finditer(r'(.)\1*',s)]
    for k in sub:
        x = len(k)
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    maj = list(d.keys())[list(d.values()).index(max(d.values()))]

    subcorr = []
    for w in sub:
        if len(w)<maj:
            continue
        elif len(w)>maj:
            subcorr.append(w[:maj])
        else:
            subcorr.append(w)

    return len(s)-len(''.join(subcorr))

n,q = map(int,input().split())
s = input()
l = []
for _ in range(q):
    l.append(list(map(int, input().split())))

for i in range(len(l)):
    print(findmin(s[l[i][0]:l[i][1]+1]))
