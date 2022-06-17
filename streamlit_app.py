import streamlit as st
#import psutil
import time
from astroquery.mast import Tesscut
from astroquery.mast import Catalogs
from astropy.coordinates import SkyCoord
from time import process_time

st.header("Tiempo de descarga de datos del portal TESScut")

t1_start = process_time()
#last_received = psutil.net_io_counters().bytes_recv
#last_sent = psutil.net_io_counters().bytes_sent
#last_total = last_received + last_sent

@st.experimental_memo(suppress_st_warning=True, show_spinner=False)
def runner(starName):
    #bytes_received = psutil.net_io_counters().bytes_recv
    #bytes_sent = psutil.net_io_counters().bytes_sent
    #bytes_total = bytes_received + bytes_sent

    st.write(starName)
    catalogData = Catalogs.query_object(starName, catalog = "TIC")
    ra = catalogData[0]['ra']
    dec = catalogData[0]['dec']
    tic = catalogData[0]['ID']
    Tmag = catalogData[0]['Tmag']
    coord = SkyCoord(ra, dec, unit = "deg")
    hdulist = Tesscut.get_cutouts(coordinates=coord, size=10)

    new_t1_start = t1_start

    t1_stop = process_time()

    final = t1_stop-new_t1_start
    final_t = '{0:.3g}'.format(final)

    st.write(final_t, "seconds")

    #new_received = bytes_received - last_received
    #new_sent = bytes_sent - last_sent

    #mb_new_received = new_received / 1024 / 1024
    #mb_new_sent = new_sent / 1024 / 1024
    #mb_new_total = new_total / 1024 / 1024

    #st.write(mb_new_received)
    #st.write(mb_new_sent)

    #last_received = bytes_received
    #last_sent = bytes_sent

list=["GM Aur", "Lambda Ori", "Sz 19", "25 Ori", "Gamma Vel", "HL Tau", "BP Tau", "Sigma Ori", "Epsilon Ori", "TX Ori"]

for i in list:
    runner(i)
    st.legacy_caching.caching.clear_cache()
