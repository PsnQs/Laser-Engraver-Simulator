import re
class StepperMotor:
    def __init__(self, x):
        self.angle = x

    
    def parseGcode(self, name=0):
        if name!=0:
            file = open(name, 'r')
            self.s = file.read().splitlines()
            file.close()
        retArray = []
        sout = [re.findall(r"[XY](.*?)[ \r\n]",sin) for sin in self.s]
        for i in range(len(self.s)):
            if self.angle == 'phi':
                if len(sout[i])==2:
                    retArray.append(sout[i][1])
                elif self.s[i][:3]=='M05':
                    retArray[-1] = retArray[-1]+'00001'
            elif self.angle == 'theta':
                if len(sout[i])==2:
                    retArray.append(sout[i][0])
                elif self.s[i][:3]=='M05':
                    retArray[-1] = retArray[-1]+'00001'
        return retArray
    

class Test: 
    def __init__(self):
        pass
    def test(self):
        print('hello')

                
