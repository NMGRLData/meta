#===============================================================================
# EXTRACTION SCRIPT obama_air_x1.py
#===============================================================================
'''
modifier: 01
eqtime: 15
'''

def main():
    info("Air Pipette x1")
    gosub('obama:WaitForMiniboneAccess')
    gosub('obama:PrepareForAirShot')
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('obama:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    close(description='Outer Pipette 2')
    
    

#===============================================================================
# POST EQUILIBRATION SCRIPT obama_pump_extraction_line.py
#===============================================================================
def main():
    info('Pump after analysis')
    gosub('obama:PumpBone')
    if get_resource_value(name='ObamaMiniboneFlag'):
        gosub('obama:PumpMinibone')
#===============================================================================
# POST MEASUREMENT SCRIPT obama_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='V')
	