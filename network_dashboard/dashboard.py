import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict
from typing import Dict, List, Optional
import time
import socket
import logging
import warnings
from packet_processor import PacketProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


