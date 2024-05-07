import matplotlib.pyplot as plt
import numpy

data = numpy.genfromtxt("down.txt")

nu = data[-2]
T = 1/nu
dU = data[-1]

#print(data)
x = list(map(lambda t: t*T, range(len(data)-2)))
y = list(map(lambda t: data[t]*dU, range(len(data)-2)))


#fig, ax = plt.subplots()
plt.plot(x,y, label = "U(t)")
#ax.set(xticks = numpy.arange(0,len(data)-2), yticks = numpy.arange(0,max(data),), xlim = (0,(len(data)-2)*T), ylim = (0,dU*max(data)))

#plt.yticks(ticks = numpy.arange(0,max(y),0.1), minor=True)
#plt.xticks(numpy.arange(0,len(data)-2,0.1),minor=True)
plt.tick_params(which="minor",alpha=0.3)
plt.grid(which="minor",alpha=0.3)
#plt.figure()
#plt.title("")
plt.xlabel("t, seconds")
plt.ylabel("U, volts")

#plt.plot(x,y)
plt.show()
