import streamlit as st
#import psutil
import time
from astroquery.mast import Tesscut
from astroquery.mast import Catalogs
from astropy.coordinates import SkyCoord
from time import process_time

st.header("Tiempo de descarga de datos del portal TESScut")

_start_time = time.time()

def tic():
    global _start_time
    _start_time = time.time()

def tac():
    t_sec = round(time.time() - _start_time)
    (t_min, t_sec) = divmod(t_sec,60)
    (t_hour,t_min) = divmod(t_min,60)
    st.write('{} seg'.format(t_sec))

@st.experimental_memo(suppress_st_warning=True, show_spinner=False)
def runner(starName):
    st.write(starName)
    catalogData = Catalogs.query_object(starName, catalog = "TIC")
    ra = catalogData[0]['ra']
    dec = catalogData[0]['dec']
    tic = catalogData[0]['ID']
    Tmag = catalogData[0]['Tmag']
    coord = SkyCoord(ra, dec, unit = "deg")
    hdulist = Tesscut.get_cutouts(coordinates=coord, size=10)
    st.legacy_caching.caching.clear_cache()


list=["GM Aur", "Lambda Ori", "Sz 19", "25 Ori", "Gamma Vel", "HL Tau", "BP Tau", "Sigma Ori", "Epsilon Ori", "TX Ori"]

for i in list:
    tic()
    runner(i)
    tac()
