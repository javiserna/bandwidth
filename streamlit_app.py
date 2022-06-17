import streamlit as st
import psutil

st.header("bandwidth usage by astropy")

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

for i in range(1000):
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    
