import math
n=148
def prime_factor(n):
	while (n%2==0):
		print(2)
		n=n/2
	for i in range(3,int(math.sqrt(n))+1,2):
		while n%i==0:
			print(i)
			n = n/i

	if n > 2:
		print (int(n))

prime_factor(n)