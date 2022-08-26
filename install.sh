#!/bin/sh

echo "Downloading required kernels. . . "
cd kernels
echo "====================================================================================="
curl -O https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp 
echo "-------------------------------------------------------------------------------------"
curl -O https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc 
echo "-------------------------------------------------------------------------------------"
curl -O https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls.pc 
echo "====================================================================================="
echo "Kernels Downloaded."