import PaletteCreator as pc
import wx

#La fenetre en elle meme
class MainFrame(wx.Frame) :
    def __init__(self) :
        super().__init__(parent=None, title="Palette Creator", size=(265,195), style=wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)
        self.SetIcon(wx.Icon(".\icon.png"))
        panel = MainPanel(self)
        self.Show()

#La "grille" sur laquelle on va fixer nos differents choix
class MainPanel(wx.Panel) :
    def __init__(self, parent) :
        #Init fraim et sizer principal
        super().__init__(parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        #Ajout du choix de shade
        shadeChoice = ShadeSelector(self)
        shadeStaticText = wx.StaticText(self, label="Shade :", style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        shadeSizer = wx.BoxSizer(wx.HORIZONTAL)
        shadeSizer.Add(shadeStaticText, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        shadeSizer.Add(shadeChoice, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        mainSizer.Add(shadeSizer, flag=wx.EXPAND, border=3)

        #Ajout du choix de mode
        modeChoice = ModeSelector(self)
        modeStaticText = wx.StaticText(self, label="Mode :", style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        modeSizer = wx.BoxSizer(wx.HORIZONTAL)
        modeSizer.Add(modeStaticText, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        modeSizer.Add(modeChoice, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        mainSizer.Add(modeSizer, flag=wx.EXPAND, border=3)

        #Ajout du choix de taille
        widthChoice = WidthSelector(self)
        widthStaticText = wx.StaticText(self, label="Width :", style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        widthSizer = wx.BoxSizer(wx.HORIZONTAL)
        widthSizer.Add(widthStaticText, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        widthSizer.Add(widthChoice, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        mainSizer.Add(widthSizer, flag=wx.EXPAND, border=3)

        #Ajout du choix de temperature
        temperatureChoice = TemperatureSelector(self)
        temperatureStaticText = wx.StaticText(self, label="Temperature :", style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        temperatureSizer = wx.BoxSizer(wx.HORIZONTAL)
        temperatureSizer.Add(temperatureStaticText, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        temperatureSizer.Add(temperatureChoice, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        mainSizer.Add(temperatureSizer, flag=wx.EXPAND, border=3)

        typeChoice = TypeSelector(self)
        typeStaticText = wx.StaticText(self, label="Type :", style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        typeSizer = wx.BoxSizer(wx.HORIZONTAL)
        typeSizer.Add(typeStaticText, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        typeSizer.Add(typeChoice, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        mainSizer.Add(typeSizer, flag=wx.EXPAND, border=3)

        #Ajout du bouton de validation
        validationButton = ValidationButton(self)
        validationSizer = wx.BoxSizer(wx.HORIZONTAL)
        validationSizer.Add(validationButton, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=1)
        mainSizer.Add(validationSizer, flag=wx.ALIGN_CENTRE_HORIZONTAL, border=3)

        #Fin de l'instanciation
        self.SetSizer(mainSizer)

class ShadeSelector(wx.Choice) :
    def __init__(self, parent) :
        shadeList = ["Red", "Yellow-red", "Yellow", "Green-yellow", "Green", "Cyan-green", "Cyan", "Blue-cyan", "Blue", "Magenta-blue", "Magenta", "Red-magenta"]
        super().__init__(parent, choices=shadeList)
        self.Bind(wx.EVT_CHOICE, self.OnChoice)
    
    def OnChoice(self, event) :
        VariableStorage.SetShade(VariableStorage, self.GetSelection())

class ModeSelector(wx.Choice) :
    def __init__(self, parent) :
        modeList = ["Pastel", "Classic", "Intense"]
        super().__init__(parent, choices=modeList)
        self.Bind(wx.EVT_CHOICE, self.OnChoice)
    
    def OnChoice(self, event) :
        selection = self.GetSelection()
        if(selection == 0) : VariableStorage.SetMode(VariableStorage, 0.1)
        elif(selection == 1) : VariableStorage.SetMode(VariableStorage, 0.5)
        elif(selection == 2) : VariableStorage.SetMode(VariableStorage, 0.9)

class WidthSelector(wx.Choice) :
    def __init__(self, parent) :
        widthList = ["Ultra narrow", "Narrow", "Wide", "Ultra wide"]
        super().__init__(parent, choices=widthList)
        self.Bind(wx.EVT_CHOICE, self.OnChoice)

    def OnChoice(self, event) :
        selection = self.GetSelection()
        if(selection==0) : VariableStorage.SetWidth(VariableStorage, 2)
        elif(selection==1) : VariableStorage.SetWidth(VariableStorage, 5)
        elif(selection==2) : VariableStorage.SetWidth(VariableStorage, 10)
        elif(selection==3) : VariableStorage.SetWidth(VariableStorage, 15)

class TemperatureSelector(wx.Choice) :
    def __init__(self, parent) :
        temperatureList = ["Hot", "Cold"]
        super().__init__(parent, choices=temperatureList)
        self.Bind(wx.EVT_CHOICE, self.OnChoice)
    
    def OnChoice(self, event) :
        selection = self.GetSelection()
        if(selection == 0) : VariableStorage.SetTemperature(VariableStorage, 1)
        elif(selection == 1) : VariableStorage.SetTemperature(VariableStorage, -1)

class TypeSelector(wx.Choice) :
    def __init__(self, parent) :
        typeList = ["Simple", "Complementary", "Split Comp.", "Analogous", "Triadic", "Tetradic", "Reverse Tet."]
        super().__init__(parent, choices=typeList)
        self.Bind(wx.EVT_CHOICE, self.OnChoice)
    
    def OnChoice(self, event) :
        selection = self.GetSelection()
        VariableStorage.SetType(VariableStorage, selection)

class ValidationButton(wx.Button) :
    def __init__(self, parent) :
        super().__init__(parent, label = "Create Palette !")
        self.Bind(wx.EVT_BUTTON, self.OnValidate)
    
    def OnValidate(self, event) :
        variables = VariableStorage.GetTheVariables(VariableStorage)
        shade = variables[0]
        mode = variables[1]
        width = variables[2]
        temperature = variables[3]
        type = variables[4]

        if(shade == -1 or mode == 0 or width == 0 or temperature == 0 or type == -1) : self.SetLabelText("ERROR!")
        else :
            if(type == 0) : pc.GenerateSingle(shade*30, mode, width, temperature)
            elif(type == 1) : pc.GenerateComplementary(shade*30, mode, width, temperature)
            elif(type == 2) : pc.GenerateSplitComplementary(shade*30, mode, width, temperature)
            elif(type == 3) : pc.GenerateAnalogous(shade*30, mode, width, temperature)
            elif(type == 4) : pc.GenerateTriadic(shade*30, mode, width, temperature)
            elif(type == 5) : pc.GenerateTetradic(shade*30, mode, width, temperature)
            elif(type == 6) : pc.GenerateReverseTetradic(shade*30, mode, width, temperature)
            
            if(self.GetLabel() == "Palette Created!") : self.SetLabelText("Palette Created!!!")
            else : self.SetLabelText("Palette Created!")

        
class VariableStorage :
    def __init__(self):
        self.shade = -1
        self.mode = 0
        self.width = 0
        self.temperature = 0
        self.type = -1
    
    def SetShade(self, s) :
        self.shade = s

    def SetMode(self, m) :
        self.mode = m

    def SetWidth(self, w) :
        self.width = w

    def SetTemperature(self, t) :
        self.temperature = t
    
    def SetType(self, t) :
        self.Type = t
    
    def GetTheVariables(self) :
        return (self.shade, self.mode, self.width, self.temperature, self.Type)

if __name__ == "__main__" :
    VariableStorage.__init__(VariableStorage)
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()