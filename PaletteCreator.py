import HSVcolor as hsv
from numpy import random as rdm
from PIL import Image
from datetime import datetime
import RGBColor as rgb

def CompensateSeuil(hue) :
    H = hue/120
    if(H < 1) : comp = (0.299/0.587)*(1-H) + H
    elif(H < 2) : comp = (2-H) + (0.114/0.587)*(H-1)
    else : comp = (0.114/0.587)*(3-H) + (0.299/0.587)*(H-2)
    return comp

def GenerateShade(hue, saturation, value, seuil, coeff) :
    cHSV = hsv.HSVcolor(hue, saturation + rdm.randint(-10, 11), value + rdm.randint(-10, 11))

    l = cHSV.GetLuminance()
    seuil *= (1-coeff) + coeff*CompensateSeuil(hue)
    seuil = round(seuil)

    while(l != seuil) :
        if(l > seuil) : cHSV.Darker()
        else : cHSV.Lighter()
        l = cHSV.GetLuminance()

    return cHSV

def GenerateFileName(shade, mode) :
    
    if(mode == .1) : path = "Pastel"
    elif(mode == .5) : path = "Classic"
    elif(mode == .9) : path = "Intense"

    shadeList = ["Red", "Yellow-red", "Yellow", "Green-yellow", "Green", "Cyan-green", "Cyan", "Blue-cyan", "Blue", "Magenta-blue", "Magenta", "Red-magenta"]
    path += shadeList[round(shade/30)]

    date = datetime.now()
    path += date.strftime("%y%m%d")
    
    path += ".png"
    return path

def GeneratePrimary(shade, mode, width, temperature) :
    pixelList = list()
    #ATTENTION
    #Si on est dans le "mauvais hemisphere", il faut inverser la temperature pour qu'elle fonctionne correctement
    if(shade >= 180) : temperature = -temperature
    shade += rdm.randint(-5, 6)
    #On cree la troisieme couleur, qui est le point de reference pour le reste de la palette
    originalCol = GenerateShade(shade, 70, 70, 153, mode)

    #On peut maintenant rajouter les pixels un par un dans notre image
    pixelList.append(GenerateShade(shade + temperature*width*2, originalCol.GetS()-15, originalCol.GetV()-20, 51, mode).GetRGBValues())
    pixelList.append(GenerateShade(shade + temperature*width, originalCol.GetS()-5, originalCol.GetV()-10, 102, mode).GetRGBValues())
    pixelList.append(originalCol.GetRGBValues())
    pixelList.append(GenerateShade(shade - temperature*width, originalCol.GetS()-10, originalCol.GetV()+10, 204, mode).GetRGBValues())

    return pixelList

def GenerateSecondary(shade, shadeOffset, mode, width, temperature, ogCols) :
    pixelList = list()
    #ATTENTION
    #Si on est dans le "mauvais hemisphere", il faut inverser la temperature pour qu'elle fonctionne correctement
    if(shade >= 180) : temperature = -temperature
    
    #On extrait les infos des couleurs originales pour avoir une base pour les nouvelles
    #Teinte n1
    ogRGB = rgb.RGBcolor(ogCols[0][0], ogCols[0][1], ogCols[0][2])
    ogHSV = ogRGB.ToHSV()
    pixelList.append(GenerateShade(ogHSV.H + shadeOffset, ogHSV.GetS(), ogHSV.GetV(), 51, mode).GetRGBValues())
    #Teinte n2
    ogRGB = rgb.RGBcolor(ogCols[1][0], ogCols[1][1], ogCols[1][2])
    ogHSV = ogRGB.ToHSV()
    pixelList.append(GenerateShade(ogHSV.H + shadeOffset, ogHSV.GetS(), ogHSV.GetV(), 102, mode).GetRGBValues())
    #Teinte n3
    ogRGB = rgb.RGBcolor(ogCols[2][0], ogCols[2][1], ogCols[2][2])
    ogHSV = ogRGB.ToHSV()
    pixelList.append(GenerateShade(ogHSV.H + shadeOffset, ogHSV.GetS(), ogHSV.GetV(), 153, mode).GetRGBValues())
    #Teinte n4
    ogRGB = rgb.RGBcolor(ogCols[3][0], ogCols[3][1], ogCols[3][2])
    ogHSV = ogRGB.ToHSV()
    pixelList.append(GenerateShade(ogHSV.H + shadeOffset, ogHSV.GetS(), ogHSV.GetV(), 204, mode).GetRGBValues())

    return pixelList

def GenerateSingle(shade, mode, width, temperature) :
    #Initialisation de l'image
    img = Image.new(mode="RGB", size=(4, 1))
    
    #On recupere les pixels
    pixels = GeneratePrimary(shade, mode, width, temperature)

    #On recupere le bon nom pour notre fichier
    path = ".\exports\Simple" + GenerateFileName(shade, mode)

    #On exporte
    img.putdata(pixels)
    img.save(path)

def GenerateComplementary(shade, mode, width, temperature) :
    #Initialisation de l'image
    img = Image.new(mode="RGB", size=(4, 2))
    
    #On recupere les pixels
    pixels = GeneratePrimary(shade, mode, width, temperature)
    pixels += GenerateSecondary(shade, 180, mode, width, temperature, pixels)

    #On recupere le bon nom pour notre fichier
    path = ".\exports\Complementary" + GenerateFileName(shade, mode)

    #On exporte
    img.putdata(pixels)
    img.save(path)

def GenerateSplitComplementary(shade, mode, width, temperature) :
    #Initialisation de l'image
    img = Image.new(mode="RGB", size=(4, 3))
    
    #On recupere les pixels
    pixels = GeneratePrimary(shade, mode, width, temperature)
    pixels += GenerateSecondary(shade, 150, mode, width, temperature, pixels)
    pixels += GenerateSecondary(shade, -150, mode, width, temperature, pixels)

    #On recupere le bon nom pour notre fichier
    path = ".\exports\SplitComp" + GenerateFileName(shade, mode)

    #On exporte
    img.putdata(pixels)
    img.save(path)

def GenerateAnalogous(shade, mode, width, temperature) :
    #Initialisation de l'image
    img = Image.new(mode="RGB", size=(4, 3))
    
    #On recupere les pixels
    pixels = GeneratePrimary(shade, mode, width, temperature)
    pixels += GenerateSecondary(shade, -30, mode, width, temperature, pixels)
    pixels += GenerateSecondary(shade, 30, mode, width, temperature, pixels)

    #On recupere le bon nom pour notre fichier
    path = ".\exports\Analogous" + GenerateFileName(shade, mode)

    #On exporte
    img.putdata(pixels)
    img.save(path)

def GenerateTriadic(shade, mode, width, temperature) :
    #Initialisation de l'image
    img = Image.new(mode="RGB", size=(4, 3))
    
    #On recupere les pixels
    pixels = GeneratePrimary(shade, mode, width, temperature)
    pixels += GenerateSecondary(shade, 120, mode, width, temperature, pixels)
    pixels += GenerateSecondary(shade, -120, mode, width, temperature, pixels)

    #On recupere le bon nom pour notre fichier
    path = ".\exports\Triadic" + GenerateFileName(shade, mode)

    #On exporte
    img.putdata(pixels)
    img.save(path)

def GenerateTetradic(shade, mode, width, temperature) :
    #Initialisation de l'image
    img = Image.new(mode="RGB", size=(4, 4))
    
    #On recupere les pixels
    pixels = GeneratePrimary(shade, mode, width, temperature)
    pixels += GenerateSecondary(shade, 60, mode, width, temperature, pixels)
    pixels += GenerateSecondary(shade, 180, mode, width, temperature, pixels)
    pixels += GenerateSecondary(shade, -120, mode, width, temperature, pixels)

    #On recupere le bon nom pour notre fichier
    path = ".\exports\Tetradic" + GenerateFileName(shade, mode)

    #On exporte
    img.putdata(pixels)
    img.save(path)

def GenerateReverseTetradic(shade, mode, width, temperature) :
    #Initialisation de l'image
    img = Image.new(mode="RGB", size=(4, 4))
    
    #On recupere les pixels
    pixels = GeneratePrimary(shade, mode, width, temperature)
    pixels += GenerateSecondary(shade, 120, mode, width, temperature, pixels)
    pixels += GenerateSecondary(shade, 180, mode, width, temperature, pixels)
    pixels += GenerateSecondary(shade, -60, mode, width, temperature, pixels)

    #On recupere le bon nom pour notre fichier
    path = ".\exports\RevTet" + GenerateFileName(shade, mode)

    #On exporte
    img.putdata(pixels)
    img.save(path)
