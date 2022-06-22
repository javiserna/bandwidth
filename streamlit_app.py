from astroquery.mast import Tesscut
from astropy.io import fits
import time
import random
import streamlit as st

st.header('TESScut download time. Randomize sectors and target sources')

for i in range(1000):
    sources=['HL Tau', 'BP Tau', 'LkCa 4', 'LkCa 9', 'Sigma Ori', 'GM Aur', 'TX Ori', 'FX Ori', 'XX Cha', 'Sz 19']
    starName = random.choice(sources)
    sectorTable = Tesscut.get_sectors(objectname=starName)
    sectors = [i for i in sectorTable['sector']]
    option = random.choice(sectors)
    start=time.time()
    hdulist = Tesscut.get_cutouts(objectname=starName, size=10, sector=option)
    hdu1 = hdulist[0]
    end=time.time()
    elapsed=(end-start)
    st.write(elapsed)
