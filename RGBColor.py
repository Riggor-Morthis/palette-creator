import HSVcolor as hsv
from math import sqrt

class RGBcolor :
    def __init__(self, red, green, blue) :
        self.R = red
        self.G = green
        self.B = blue
    
    def PrintSelf(self) :
        print("r:",round(self.R*255)," g:",round(self.G*255)," b:",round(self.B*255))
    
    def ToHSV(self) :
        Cmax = max(self.R, self.G, self.B)
        Cmin = min(self.R, self.G, self.B)
        Delta = Cmax - Cmin

        if(Cmax == Cmin) : h = 0
        elif(Cmax == self.R) : h = (60 * ((self.G - self.B)/Delta)+360) % 360
        elif(Cmax == self.G) : h = (60 * ((self.B - self.R)/Delta)+120) % 360
        elif(Cmax == self.B) : h = (60 * ((self.R - self.G)/Delta)+240) % 360

        if(Cmax == 0) : s = 0
        else : s = (Delta/Cmax)

        v = Cmax

        return hsv.HSVcolor(round(h), round(s*100), round(v*100))
    
    def GetValues(self) :
        return (round(self.R*255), round(self.G*255), round(self.B*255))
    
    def GetLuminance(self) :
        value = (0.299*self.R + 0.587*self.G + 0.114*self.B)*255
        return round(value)