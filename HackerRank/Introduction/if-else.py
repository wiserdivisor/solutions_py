n=int(input())
check={1:"Not Weird",0:"Weird"}
print(check[(n%2==0)and(n in range(2,6)or n>20)])
