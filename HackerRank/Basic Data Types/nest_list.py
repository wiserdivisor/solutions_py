lst=[[input(),float(input())]for _ in range(int(input()))]
sh=sorted(list(set([m for n,m in lst])))[1]
print('\n'.join([n for n,m in sorted(lst) if m==sh]))
