from BEC import BinaryErasureChannel as BEC
import math
import numpy as np
import utility

channel = BEC(alpha = 0.7)
n = int((math.pow(2, 11) * 0.1))
x = np.random.binomial(1, 0.5, n)

I  = channel.polarize(int(math.pow(2, 11)), 0.9999888)
l = range(int(math.pow(2, 11)))
Ineg = [-I[i] for i in range(len(I))]
polarized = [True for i in range(len(I))]
I1, l1 = zip(*sorted(zip(Ineg,l)))
inp = [0 for i in range(int(math.pow(2,11)))]

for i in range(len(x)):
	inp[l1[i]] = x[i] 
	polarized[i] = False

inp = np.random.binomial(1, 0.5, int(math.pow(2, 11)))

encoded = utility.encode(inp)

y = channel.passInput(encoded)

decoded = utility.decode(y)

c = 0
for i in range(len(inp)):
	if(not polarized[i]):
		if(decoded[i] == inp[i]):
			c+=1

print n, c


