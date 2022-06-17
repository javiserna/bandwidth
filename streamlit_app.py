import streamlit as st
import time
from astroquery.mast import Tesscut
from astroquery.mast import Catalogs
from astropy.coordinates import SkyCoord
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                div[data-testid="stToolbar"] {visibility: hidden;}
                div[data-testid="stDecoration"] {visibility: hidden;}
                div[data-testid="stStatusWidget"] {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("Tiempo de descarga promedio de datos para 10 estrellas")

_start_time = time.time()

def tic():
    global _start_time
    _start_time = time.time()

def tac():
    t_sec = round(time.time() - _start_time)
    (t_min, t_sec) = divmod(t_sec,60)
    (t_hour,t_min) = divmod(t_min,60)
    st.write('{} seg'.format(t_sec))
    return t_sec

@st.experimental_memo(suppress_st_warning=True, show_spinner=False)
def runner(starName):
    st.info('Estrella:', starName)
    catalogData = Catalogs.query_object(starName, catalog = "TIC")
    ra = catalogData[0]['ra']
    dec = catalogData[0]['dec']
    tic = catalogData[0]['ID']
    Tmag = catalogData[0]['Tmag']
    coord = SkyCoord(ra, dec, unit = "deg")
    hdulist = Tesscut.get_cutouts(coordinates=coord, size=10)
    st.legacy_caching.caching.clear_cache()


list=["GM Aur", "Lambda Ori", "Sz 19", "25 Ori", "Gamma Vel", "HL Tau", "BP Tau", "Sigma Ori", "Epsilon Ori", "TX Ori"]
a=[]

for i in list:
    tic()
    runner(i)
    a.append(tac())

in1 = plt.figure(1)
plt.hist(a, bins='auto', color = 'red')
plt.xlabel('Tiempo (Segundos)')
st.pyplot(in1)
