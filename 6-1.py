import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


GPIO.setmode(GPIO.BCM)

dig = 8
U0 = 3.3
dac = [8,11,7,1,0,5,12,6]

leds = [2,3,4,17,27,22,10,9]

comp = 14
troyka = 13
for a in dac + leds:
	GPIO.setup(a,GPIO.OUT)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(troyka,GPIO.OUT)
GPIO.output(troyka, 1)


def dec2bin(x):
	a = []
	for i in range(dig):
		a = [x%2]+a
		x=x//2
	return a

def bin2dec(x):
	y = 0
	for i in range(dig):
		y = y + x[-1-i]*2**i
	return y
		

def setpins(n, bins):
	for i in range(dig):
		GPIO.output(n[i], bins[i])
"""
def adc1():
	for x in range(2**dig):
		setpins(dec2bin(x))
		time.sleep(0.005)
		if GPIO.input(comp):
			return x
	return 256
"""	
def adc():
	x = dec2bin(0)
	y = dec2bin(0)
	for i in range(dig):
		x[i]=1
		setpins(dac, x)
		time.sleep(0.003)
		if GPIO.input(comp):
			x[i]=0
		else:
			y[i]=1
		if i>0 and y[i-1]==1:
			y[i]=1
	setpins(leds, y)
	return bin2dec(x)+1
data = []
try:
	start = 0 
	while True:
		x = adc()
		if(not start):
			start = time.time()
		data = data + [x]
		time.sleep(0.003)
		print(x,"  ",x/(2**dig)*U0)
except KeyboardInterrupt:
	print("program interrupted")

finally:
	end = time.time()
	setpins(leds, dec2bin(0))
	with open("res.txt","w") as res:
		res.write("\n".join(list(map(lambda t: str(t),data))))
		res.write("\n\n")
		res.write(str(len(data)/(end-start)))
		res.write("\n")
		res.write(str(U0/(2**dig)))
	print(end-start)
	print(len(data)/(end-start))
	setpins(dac, dec2bin(0))
	plt.plot(data)
	plt.show()
