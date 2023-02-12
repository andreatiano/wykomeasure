import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide")
plotCol, dataCol = st.columns([2,1])
importExp=st.sidebar.expander('Import Option')
Delimiter= importExp.selectbox('Delimiter:',('\t',';',','))
spectra = importExp.file_uploader("upload file",accept_multiple_files=True)
list=[]
dataset=[]
data=[]
if spectra is not None:
#              columnNumber=spectra_df.columns.get_loc(column[0]) 
             i=0
             st.write(len(spectra))
             spectrafor_df = pd.read_csv(spectra[0])
             spectrafor_df1 = pd.read_csv(spectra[1])
             spectrafor_df2 = pd.read_csv(spectra[2])
             spectrafor_df3 = pd.read_csv(spectra[2])
             st.write(spectra[0])
             st.write(spectrafor_df)
             st.write(spectrafor_df1)
             st.write(spectrafor_df2)
             st.write(spectrafor_df3)
             
