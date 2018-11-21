import numpy as np
import math
class BinaryErasureChannel:
	def __init__(self, alpha):
		self.alpha = alpha

	def passInput(self, inp):
		out = [-1 for i in range(len(inp))]
		for i in range(len(inp)):
			x = np.random.uniform(low = 0.0, high  = 1.0)
			if(x>self.alpha):
				out[i] = inp[i]

		return out
	def polarize(self, N, thresh):
		I = []
		alpha = 0.7
		I.append(1 - alpha)
		t = 1
		Ilist = []
		for n in range(1, int(math.log(N, 2))+1):
			Ilist.append(I)
			t *= 2
			Iprev = I
			I = []
			# print n
			for i in range(0, t/2):
				I.append(Iprev[i]*Iprev[i])
				I.append(2*Iprev[i] - Iprev[i]*Iprev[i])
		return I#, [(I[i]>=thresh or I[i]<=1-thresh) for i in range(len(I))]



