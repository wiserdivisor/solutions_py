s = input()
out = ""
flag = True
for i in s:
    if  (i=='G'):out+='C'
    elif(i=='C'):out+='G'
    elif(i=='A'):out+='U'
    elif(i=='U'):out+='A'
    elif(i=='T'):out+='A'
    else:
        flag = False
        print("Invalid Input")
        break
print(out*flag)
