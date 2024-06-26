from .tempProfile import tempProfile
from .densityProfile import densityProfile
from .salinityProfile import salinityProfile

class HolteAndTalley:
    def __init__(self,pressures,temperatures,salinities,densities):
        self.temp = tempProfile(pressures,temperatures)
        self.tempMLD = self.temp.findMLD()
        if len(salinities) != 0 and len(densities) != 0:
            self.salinity =  salinityProfile(pressures,temperatures,salinities,densities,self.temp)
            self.salinityMLD = self.salinity.findMLD()
            self.density = densityProfile(pressures,temperatures,salinities,densities,self.temp,self.salinity)
            self.densityMLD = self.density.findMLD()

