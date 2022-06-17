import streamlit as st
import psutil

st.header("bandwidth usage by astropy")

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent

    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    #mb_new_total = new_total / 1024 / 1024

    st.write(mb_new_received)

    last_received = bytes_received
    last_sent = bytes_sent

    time.sleep (1)
