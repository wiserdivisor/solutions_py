import string
import secrets
def make_token(n):
	set = string.ascii_letters+string.digits
	while True:
		token = ''.join(secrets.choice(set) for i in range(n))
		if(any(c.islower() for c in token) and
		   any(c.isupper() for c in token) and
		   sum(c.isdigit() for c in token)>=3 ):
		   break
	return token
t = int(input("tstcases :"))
while (t!=0):
	print(make_token(int(input("Length of token :"))))
	t-=1
