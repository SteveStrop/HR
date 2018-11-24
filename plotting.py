import pylab as plt
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []
for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


plt.plot(mySamples,myLinear,'o-',label="Lin")
plt.subplot(221)
plt.plot(mySamples,myQuadratic,'r^',label="Quad")
plt.subplot(221)
plt.legend()
plt.plot(mySamples,myCubic,'go-',label="Cubic",linewidth=4)

plt.ylim(0,5000)
plt.plot(mySamples,myExponential,label="Expo")

plt.show()

