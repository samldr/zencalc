@ECHO OFF
TITLE Kernel Installer
ECHO Downloading required kernels. . . 
mkdir kernels
cd kernels
ECHO =====================================================================================
curl https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp -o de430.bsp
ECHO -------------------------------------------------------------------------------------
curl https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc -o pck00010.tpc
ECHO -------------------------------------------------------------------------------------
curl https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls.pc -o naif0012.tls.pc
ECHO =====================================================================================
ECHO Kernels Downloaded.
PAUSE