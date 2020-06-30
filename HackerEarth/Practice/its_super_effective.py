import json

with open('effectiveness.json') as f:
    d = json.load(f)

def pokemon(list1, list2):
    global d
    pointlist = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            templist = []
            for k in range(len(list1[i])):
                temp = 1
                for l in range(len(list2[j])):
                    for key,val in { "super effective":2, "normal effective":1,
                                     "not very effective":0.5, "no effect":0}.items():
                        if list2[j][l] in d[key][list1[i][k]]:
                            temp *= val
                templist.append(temp)
            pointlist.append(max(templist))
    return sum(pointlist)


m = int(input())
f = int(input())

mylist = []
opplist = []

for i in range(m+f):
    if(i>m-1):
        opplist.append(input().split())
    else:
        mylist.append(input().split())

mypoints = float(pokemon(mylist, opplist))
oppoints = float(pokemon(opplist, mylist))

print(mypoints,oppoints, sep='\n')

if(mypoints==oppoints):print("EQUAL")
elif(mypoints>oppoints):print("ME")
else:print("FOE")
