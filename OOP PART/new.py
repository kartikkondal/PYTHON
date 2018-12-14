class BMW:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

class ThreeSeries(BMW):
    def __init__(self,CruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.CruiseControledEnabled = CruiseControlEnabled

    def Showcase(self):
        print("make ==>",self.make,"model ==>",self.model,"year ==>",self.year,"CruiseControledEnabled ==>",self.CruiseControledEnabled)

class FiveSeries(BMW):
    def __init__(self,ParkingAssistantEnabled,make,model,year):
        super()._init__(make,model,year)
        self.ParkingAssistantEnabled = ParkingAssistantEnabled
    def Showcase(self):
        print("make ==>",self.make,"model ==>",self.model,"year ==>",self.year,"PasrkingAssistantEnabled ==>",self.ParkingAssistantEnabled)

threeseries = ThreeSeries(True,'BMW','i329',2018)
fiveseries = FiveSeries(True,'Audi','i123',2017)
threeseries.Showcase()
fiveseries.Showcase()

