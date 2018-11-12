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


# inp = [1, 1]
inp = [0, 1, 0, 1]#, 0, 1, 0, 1]
print encode(inp)
