l = []
for i in range(int(input())):
    l.append(list(map(int, input().split())))
    for _ in range(l[i][1]):
        l[i].append(list(map(int, input().split())))
