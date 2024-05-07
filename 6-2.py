import matplotlib.pyplot as plt
import numpy

data = numpy.genfromtxt("res.txt")

nu = data[-2]
T = 1/nu
dU = data[-1]

#print(data)
x = list(map(lambda t: t*T, range(len(data)-2)))
y = list(map(lambda t: data[t]*dU, range(len(data)-2)))


fig, ax = plt.subplots()
ax.grid(True)
ax.plot(x,y)
ax.set(xticks = numpy.arange(len(data)-2), yticks = numpy.arange(max(data)), xlim = (0,(len(data)-2)*T), ylim = (0,dU*max(data)))


#plt.figure()
#plt.title("")
plt.xlabel("t, seconds")
plt.ylabel("U, volts")

#plt.plot(x,y)
plt.show()
