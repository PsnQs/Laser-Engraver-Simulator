import math

def helloWorld():
    print("Hello world!")


def loadGcode(name):
    file = open(name,"r")
    s = file.read()
    file.close()
    return s.splitlines()

def linearToAngle(x, y, midX, midY):
    x-=midX
    y-=midY
    theta = math.atan(y/x)
    if theta<0:
        theta+=math.pi
    if y<0:
        theta+=math.pi
    theta+=math.pi
    theta = theta%(2*math.pi)
    phi = math.atan(math.sqrt(x**2+y**2)/150)
    #theta = 'test'
    #phi = 'test'
    return [theta, phi]
    

