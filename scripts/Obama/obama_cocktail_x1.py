#===============================================================================
# EXTRACTION SCRIPT obama_cocktail_x1.py
#===============================================================================
'''
modifier: 01
eqtime: 15
'''

def main():
    info("Cocktail Pipette x1")
    gosub('obama:WaitForMiniboneAccess')
    gosub('obama:PrepareForAirShot')
    gosub('common:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('obama:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette1')
    close(description='Outer Pipette 1')
    
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
	