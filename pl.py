import random

chars = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,./;'[]!@#$%^&*()_+~\|:"<>?'''
times = int(input('[.]Number of passwords?\n[.]'))
length = int(input('[.]Password length?\n[.]'))

f = open('password.txt asdadshajsdkajdskahskd','w')

for i in range(times):
	password = ''
	for j in range(length):
		password += random.choice(chars)



SPURSSSSSS



	print('[.]',password,sep='')
	
	
	password = password + '\n'
	f.write(password)

f.close()


