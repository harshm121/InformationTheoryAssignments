class Polarize:
	def __init__(self, alpha):
		self.alpha = alpha
		
# from matplotlib import pyplot as plt
I = []
alpha = 0.7
I.append(1 - alpha)
N = 1
Ilist = []
for n in range(1, 31):
	Ilist.append(I)
	N *= 2
	Iprev = I
	I = []
	print n
	for i in range(0, N/2):
		I.append(Iprev[i]*Iprev[i])
		I.append(2*Iprev[i] - Iprev[i]*Iprev[i])


# for i in range(len(Ilist)):
# 	plt.figure(figsize=(20,20))
# 	plt.bar(range(1, len(Ilist[i])+1), Ilist[i], width = 0.35)
# 	# plt.xticks(range(1, len(Ilist[i])+1), range(1, len(Ilist[i])+1))
# 	plt.ylabel("I(channel)")
# 	plt.xlabel("N")
# 	plt.savefig('./figures/'+str(i)+'.png')	
# 	plt.clf()

# Iless = []
# Imore = []
# n = []
# x = 1
# for i in range(len(Ilist)):
# 	I = Ilist[i]
# 	Iless.append(((sum([I[j]<0.01 for j in range(len(I))]*1))+0.)/len(I)*100)
# 	Imore.append(((sum([I[j]>0.99 for j in range(len(I))]*1))+0.)/len(I)*100)
	# n.append(x)
	# x*=2

# plt.plot(n, Iless)
# plt.plot(n, Imore)
# plt.legend(["number of channels with I<0.2", "number of channels with I>0.8"])
# p1 = plt.bar(range(1, len(Ilist)+1), Iless, 0.35, )
# p2 = plt.bar(range(1, len(Ilist)+1), Imore,0.35, bottom = Iless)
# plt.xticks(range(len(Ilist)),range(len(Ilist)) )
# plt.savefig("./figures/thisIsNiceBar.jpg")


# for i in range(len(Ilist)):
# 	x = range(1, len(Ilist[i])+1)
# 	y = Ilist[i]
# 	plt.figure(figsize=(22,22))
# 	plt.scatter(x, y, c='r', marker= '*')
# 	plt.savefig('./figures/'+str(i+1)+'.png')
# 	plt.clf()
# 	