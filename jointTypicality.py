import numpy as np
import math
# import matplotlib.pyplot as plt
class Channel:
	def __init__(self, p):
		self.transitionProbability = p

	def transmit(self, inp):
		x = np.random.uniform(low = 0.0, high = 1.0)
		# print x
		if(x<=self.transitionProbability):
			# if(inp==1):
			# 	return 0
			# else:
			# 	return 1
			return inp ^ 1

		else:
			return inp

	def transmitSeq(self, inp):
		out = []
		for i in range(len(inp)):
			out.append(self.transmit(inp[i]))
		return out

	def getChannelCapacityEmperically(self, px1low, px1high, step):
		IxyList = []
		px1List = []
		N=50000
		for i in range(int((px1high-px1low)/step)+1):
			px1 = px1low + step*i
			inp = getInputSeq(px1, N)
			out = self.transmitSeq(inp)
			Hy = getEntropy(out)
			inp0 = getInputSeq(0, N)
			Hygivenx0 = getEntropy(self.transmitSeq(inp0))
			inp1 = getInputSeq(1, N)
			Hygivenx1 = getEntropy(self.transmitSeq(inp1))
			Hygivenx = ((sum(inp)+0.)/len(inp))*Hygivenx1 +(1-((sum(inp)+0.)/len(inp)))*Hygivenx0
			Ixy = Hy - Hygivenx
			px1List.append(px1)
			IxyList.append(Ixy)
		# plt.plot(px1List, IxyList)
		# plt.ylabel("I(X;Y)")
		# plt.xlabel("p(x=1)")
		a = IxyList.index(max(IxyList))
		# plt.annotate('max I(X;Y) = '+str(IxyList[a]) , xy=(px1List[a],IxyList[a]))
		# plt.show()
		return IxyList[a]
	def getChannelCapacityTheoretically(self):
		if(self.transitionProbability == 0):
			Hp = -(1-self.transitionProbability)*math.log((1-self.transitionProbability), 2)
		elif(self.transitionProbability == 1):
			Hp = -self.transitionProbability*math.log(self.transitionProbability, 2)
		else:
			Hp = -(1-self.transitionProbability)*math.log((1-self.transitionProbability), 2) -self.transitionProbability*math.log(self.transitionProbability, 2)
		return (1-Hp)

def getInputSeq(px1, length):
	inp = []
	for i in range(length):
		x = np.random.uniform(low = 0.0, high = 1.0)
		if(x<=px1):
			inp.append(1)
		else:
			inp.append(0)
	return inp

def getEntropy(seq):
	p1 = (sum(seq)+0.)/len(seq)
	p0 = 1-p1
	if(p0 ==0):
		return -p1*math.log(p1, 2)
	elif(p1 == 0):
		return -(p0*math.log(p0, 2))
	else:
		return (-(p0*math.log(p0, 2) + p1*math.log(p1, 2)))


def jointTypicality(xn, yn, e, px1, p, Hx, Hxy):
	n = len(xn)
	sx = sum(xn)	
	pxn = [math.pow(px1, sx), math.pow((1-px1), n-sx)]
	pxnl = [-(math.log(pxn[i], 2))/n for i in range(2)]
	pxn = sum(pxnl)
	px = abs(pxn - Hx)<e
	if(not px):
		return False

	s = sum(([xn[i]==yn[i] for i in range(len(xn))])*1)

	pxnyn = [math.pow((1-p), s), math.pow(p, (n-s)), math.pow(px1, sx), math.pow((1-px1), (n-sx))]
	pxnynl = [-(math.log(pxnyn[i], 2))/n for i in range(4)]
	pxnyn = sum(pxnynl)
	pxy = abs(pxnyn - Hxy) < e
	# print abs(-(math.log(pxnyn, 2))/n - Hxy), e
	# print ".",
	return pxy


def decode(codeBook, yn, e, px1, py1, p, Hx, Hy, Hxy):

	pyn = [math.pow(py1, sum(yn)), math.pow((1-py1), n-sum(yn))]
	pynl = [-(math.log(pyn[i], 2))/n for i in range(2)]
	pyn = sum(pynl)
	py = abs(pyn - Hy)<e
	if(not py):
		return -1

	decoded = -1
	onlyOne = False
	for i in range(len(codeBook)):
		if(jointTypicality(codeBook[i], yn, e, px1, p, Hx, Hxy)):
			decoded = i
			if(not onlyOne):
				onlyOne = True
			else:
				return -1
	return decoded

channel = Channel(p = 0.4)

#Channel Capacity
C = channel.getChannelCapacityTheoretically()
print "Capacity (Calculated Emperically) of our channel is: " +str(channel.getChannelCapacityEmperically(0.0, 1.0, 0.1))
print "Capacity (Calculated Theoretically) of our channel is: " + str(C)

#Codebook
nList = [10, 50, 100, 500, 600, 700, 800, 1000]
probOfError = []
R = C/2
px1 = 0.5
py1 = px1*(1-channel.transitionProbability) + (1-px1)*channel.transitionProbability
p = channel.transitionProbability
e = 0.03
Hx = -px1*math.log(px1, 2) - (1-px1)*math.log((1-px1), 2)
Hy = -py1*math.log(py1, 2) - (1-py1)*math.log((1-py1), 2)
Hygivenx0 = -p*math.log(p, 2) - (1-p)*math.log(1-p, 2)
Hygivenx1 = Hygivenx0
Hygivenx = px1*Hygivenx1 + (1-px1)*Hygivenx0
Hxy = Hx + Hygivenx

for n in nList:
	print "n = ", n
	codeBook = []
	for i in range (int(math.ceil(math.pow(2, n*R)))):
		codeBook.append(getInputSeq(px1, n))
	print len(codeBook)
	output = []

	for i in range(len(codeBook)):
		output.append(channel.transmitSeq(codeBook[i]))
	print "output recieved"
	# pxy = [[0,0], [0,0]]
	# pxy[0][0] = (1-p)*(1-px1)
	# pxy[0][1] = p*(1-px1)
	# pxy[1][0] = px1*(1-p)
	# pxy[1][1] = p*px1

	corr = 0
	corrpy = 0
	corrjt = 0
	for i in range(len(output)):
		if((i+1)%5000==0):
			print i+1 ," decoded"
		ihat = decode(codeBook, output[i], e, px1, py1, p, Hx, Hy, Hxy)
		if(ihat == i):
			corr +=1
		# yn = output[i]
		# pyn = [math.pow(py1, sum(yn)), math.pow((1-py1), n-sum(yn))]
		# pynl = [-(math.log(pyn[i], 2))/n for i in range(2)]
		# pyn = sum(pynl)
		# py = abs(pyn - Hy)<e
		# if(py):
		# 	if(jointTypicality(codeBook[i], yn, e, px1, p, Hx, Hxy)):
		# 		corr+=1
		# 	else:
		# 		corrjt +=1
		# else:
		# 	corrpy +=1

	# print corr, corrjt, corrpy
	print (corr+0.)/len(output)
	probOfError.append(1-(corr+0.)/len(output))	

print nList
print probOfError




