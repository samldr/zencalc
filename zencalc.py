import os
import math
import json
import spiceypy as spice
from datetime import datetime

def zencalc(date):

    # I/O:
    #   I: Desired Date (as string yyyy-mm-dd hh:mm:ss)
    #   O: Position of Zenith (appended json)

    spice.furnsh('kernels\\naif0012.tls.pc') if os.name == 'nt' else spice.furnsh('kernels\\naif0012.tls') #leapseconds 
    spice.furnsh('kernels\\de430.bsp') #planets spk
    spice.furnsh('kernels\\pck00010.tpc') #orientation pck

    with open('output.json', 'r') as file:
        pdict = json.load(file)

    for i in pdict['bodies']:

        zenpos = spice.subpnt('NEAR POINT/ELLIPSOID', 'EARTH', spice.str2et(date), 'IAU_EARTH', 'CN+S', str(i['ID']))
        latlong = spice.reclat(zenpos[0])
        coords = [math.degrees(latlong[2]), math.degrees(latlong[1] - math.pi/2)]

        i.update({"coordinates":coords})

    with open('output.json', 'w') as file:
        json.dump(pdict, file)
    
    spice.kclear()

#testing only
date = str(datetime.now())
zencalc(date)