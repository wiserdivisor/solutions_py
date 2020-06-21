import re

d = dict()
s = ''.join(sorted(input()))

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

print(len(s)-len(''.join(subcorr)))
