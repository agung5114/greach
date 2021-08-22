import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go
from PIL import Image
import streamlit.components.v1 as components
# import matplotlib.pyplot as plt
import pickle
# load model 
import joblib
# import bz2
# import pickle
# import _pickle as cPickle
# from extract import getBagian, extract_pasal,getBagian2, extract_pasal2
# [theme]
# base="light"
# primaryColor="purple"

st.set_page_config(layout='wide')

def main():
        st.subheader("One reliable place for keeping your documents")
        # iris= Image.open('iris.png')
        data = st.file_uploader('Upload File PDF',type='.pdf')
        if data == None:
            st.write('Please choose pdf file to upload')
        else:
            st.write('File succesfully uploaded')
  
if __name__=='__main__':
    main()
