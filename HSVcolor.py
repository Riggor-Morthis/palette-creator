import RGBColor as rgb
from numpy import random as rdm

class HSVcolor :
    def __init__(self, hue, saturation, value) :
        if(hue >= 360) : self.H = hue - 360
        elif(hue < 0) : self.H = hue + 360
        else : self.H = hue
        
        if(saturation > 100) : self.S = 1
        elif(saturation < 0) : self.S = 0
        else : self.S = saturation/100

        if(value > 100) : self.V = 1
        elif(value < 0 ) : self.V = 0
        else : self.V = value/100
    
    def PrintSelf(self) :
        print("h:",self.H," s:",round(self.S*100)," v:",round(self.V*100))
    
    def ToRGB(self) :
        c = self.V * self.S
        h = self.H / 60.0
        x = c * (1 - abs(h % 2 - 1))

        if(h < 1) :
            R1 = c
            G1 = x
            B1 = 0
        elif(h < 2) :
            R1 = x
            G1 = c
            B1 = 0
        elif(h  < 3) :
            R1 = 0
            G1 = c
            B1 = x
        elif(h < 4 ) :
            R1 = 0
            G1 = x
            B1 = c
        elif(h < 5) :
            R1 = x
            G1 = 0
            B1 = c
        elif(h < 6) :
            R1 = c
            G1 = 0
            B1 = x
        
        m = self.V - c
        return rgb.RGBcolor(R1+m, G1+m, B1+m)
    
    def GetRGBValues(self) :
        return self.ToRGB().GetValues()

    def Darker(self) :
        self.S += (rdm.randint(0,3))/100
        self.V -= (rdm.randint(0,3)+1)/100
        if(self.S > 1) : self.S = 1
        if(self.V < 0) : self.V = 0
    
    def Lighter(self) :
        self.S -= (rdm.randint(0,3))/100
        self.V += (rdm.randint(0,3)+1)/100
        if(self.S < 0) : self.S = 0
        if(self.V > 1) : self.V = 1

    def GetLuminance(self) :
        return self.ToRGB().GetLuminance()
    
    def GetS(self) :
        return round(self.S*100)
    
    def GetV(self) :
        return round(self.V*100)