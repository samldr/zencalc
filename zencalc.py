import math
import spiceypy as spice
from datetime import datetime

def zencalc(date, body):

    # I/O:
    #   I: Desired Date (as string yyyy-mm-dd hh:mm:ss)
    #   I: Desired Planet/Moon (string ID using the following numbers:
    #
    #       MERCURY BARYCENTER (1)  SATURN BARYCENTER (6)   MERCURY (199)
    #       VENUS BARYCENTER (2)    URANUS BARYCENTER (7)   VENUS (299)
    #       EARTH BARYCENTER (3)    NEPTUNE BARYCENTER (8)  MOON (301)
    #       MARS BARYCENTER (4)     PLUTO BARYCENTER (9)    EARTH (399)
    #       JUPITER BARYCENTER (5)  SUN (10))     
    #
    #   O: Position of Zenith (int array in longitude and latitude)

    spice.furnsh("kernels\\naif0012.tls.pc") #leapseconds
    spice.furnsh("kernels\\de430.bsp") #planets spk
    spice.furnsh("kernels\\pck00010.tpc") #orientation pck

    zenitpos = spice.subpnt("NEAR POINT/ELLIPSOID", "EARTH", spice.str2et(date), "IAU_EARTH", "CN+S", body)
    latlong = spice.reclat(zenitpos[0])
    coords = [math.degrees(latlong[2]), math.degrees(latlong[1] - math.pi/2)]

    print(coords)

    spice.kclear()


#testing only
body = input("Enter Body ID: ")
date = str(datetime.now())

zencalc(date, body)