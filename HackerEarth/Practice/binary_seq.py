for _ in range(int(input())):
    x,y,a,b = map(int,input().split())
    print("Yes"*(x*y==a+b)or"No")
