import math
p = []
def isPrime(n):
	s = 0
	for i in range(2,int(math.sqrt(n))+1):
		if (n % i == 0):
			s += 1
	if(s == 0):
		return True
	else:
		return False

def p_factor(x):
	for j in range(3,int(math.sqrt(x))+1,2):
		if isPrime(j):
			if(x % j == 0):
				p.append(j)

	return max(p)

#print(p_factor(13195))
print(p_factor(600851475143))
print(p)