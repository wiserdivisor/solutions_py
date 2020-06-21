y=int(input())
check={1:"True",0:"False"}
print(check[(y%4==0)and((y%400==0)or(y%100!=0))])
