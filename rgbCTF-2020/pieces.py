def conv(string):
	res=''
	for i in range(len(string)):
		if(string[i]=='|'):
			res+=chr(ord(string[i-1])*2)
		elif(string[i]=='/'):
			res+=chr(ord(string[i-1])*2+1)
	print(res)
s=input()
conv(s)
