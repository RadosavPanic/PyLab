from scapy.all import *
import streamlit as st
import plotly.graph_objects as go
from collections import defaultdict
from typing import Dict, List, Optional
import time, socket, warnings, threading
from packet_processor import PacketProcessor
from visualize_dashboard import create_visualizations

def start_packet_capture():
    """Start packet capture in a separate thread"""

    processor = PacketProcessor()

    def capture_packets():
        sniff(prn=processor.process_packet, store=False)

    capture_thread = threading.Thread(target=capture_packets, daemon=True)
    capture_thread.start()

    return processor


def main():
    """Main function to run the dashboard"""

    st.set_page_config(page_title="Network Traffic Analysis", layout="wide")
    st.title("Real-time Network Traffic Analysis")

    # Initialize packet processor in session state
    if 'processor' not in st.session_state:
        st.session_state.processor = start_packet_capture()
        st.session_state.start_time = time.time()

    # Create dashboard layout
    col1, col2 = st.columns(2)

    # Get current data
    df = st.session_state.processor.get_dataframe()

    # Display metrics
    with col1:
        st.metric("Total Packets", len(df))
    with col2:
        duration = time.time() - st.session_state.start_time
        st.metric("Capture Duration", f"{duration:.2f}s")

    # Display visuals
    create_visualizations(df)

    # Display recent packets
    st.subheader("Recent Packets")
    if len(df) > 0:
        st.dataframe(
            df.tail(10)[['timestamp', 'source', 'destination', 'protocol', 'size']]
        )

    # Add refresh button
    if st.button("Refresh data"):
        st.rerun()

    # Auto refresh
    time.sleep(2)
    st.rerun()

main()