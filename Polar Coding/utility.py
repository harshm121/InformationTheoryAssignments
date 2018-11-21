import numpy as np
import math 

def encode_utility(inp, j):
	# print inp, "utility input"
	out = [-1 for i in range(len(inp))]
	n = len(inp)
	for i in range(n/2):
		# print i+j, i+(n/2)+j
		out[i] = inp[i]^inp[i+(n/2)]
	for i in range(n/2, n):
		out[i] = inp[i] 
	# print out
	return out

def encode(inp):
	N = len(inp)
	n = N
	temp1 = inp
	temp2 = []
	while(n>=2):
		J = N/n
		for j in range(J):
			temp2.extend(encode_utility(temp1[j*n:(j+1)*n], j*n))
		# print temp2
		temp1 = temp2
		temp2 = []
		n = n/2

	return temp1

def decode(y):
	N = len(y)
	n = int(math.log(N, 2))
	u = np.zeros((n, N))
	p = np.zeros((n+1, N))
	
	for i in range(N):
		if(y[i] == 1):
			p[n][i] = 1.0
		elif(y[i] == 0):
			p[n][i] = 0.0
		else:
			p[n][i] = 0.5
	
	# for i in range(N):
	# 	for t in range(1, n):
	# 		for j in range(int(math.pow(2, t) * int( (i+0.)/math.pow(2,t) ))):
	# 			print j, "j"
	# 			u[t][j] = u[t-1][l]

	for upperIndex in range(int(math.log(N, 2))-1, -1, -1):
		s = int(math.pow(2, upperIndex))
		nn = int(math.pow(2, upperIndex+1))
		for i in range(N):
			if(i%nn < nn/2):
				p1 = p[upperIndex+1][i]
				p2 = p[upperIndex+1][i+s]
				q =  (1 - (1-2*p1)*(1-2*p2))/2
				if(q>0.5):
					u[upperIndex][i] = 1
				else:
					u[upperIndex][i] = 0
			else:
				p1 = p[upperIndex+1][i]
				p2 = p[upperIndex+1][i-s]
				u1 = u[upperIndex][i-s]
				if(u1 == 1):
					p1 = 1-p1
				q = (p1*p2)/(p1*p2 + (1-p1)*(1-p2))
				if(q>0.5):
					u[upperIndex][i] = 1
				else:
					u[upperIndex][i] = 0
	return u[0]




















