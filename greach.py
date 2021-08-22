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
        st.subheader("A reliable place for keeping your documents save")
        # iris= Image.open('iris.png')
        st.write('Upload your National Identification Card') 
        ktp = st.file_uploader('Upload File',type=['png','jpeg'])
        if ktp == None:
            st.write('Please choose file to upload')
        else:
            st.write('File succesfully uploaded')
        
        st.write('Upload your Latest Photo') 
        foto = st.file_uploader('Upload Photo',type=['png','jpeg'])
        if foto == None:
            st.write('Please choose file to upload')
        else:
            st.write('File succesfully uploaded')
        
        st.write('Upload your Transaction records') 
        data = st.file_uploader('Upload Data',type='xslx')
        if data == None:
            st.write('Please choose file to upload')
        else:
            st.write('File succesfully uploaded')
        
  
if __name__=='__main__':
    main()
