import streamlit as st
import psutil

st.header("bandwidth usage by astropy")

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

ho
