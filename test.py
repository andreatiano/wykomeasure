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
spectra_df = pd.read_csv(spectra[0])
if spectra_df is not None:
     rows = plotCol.multiselect(
     'select the row of the first measure',spectra_df.index) 
     column = plotCol.multiselect(
     'select the correct column',spectra_df.columns.values.tolist())  
#      plotCol.write(spectra_df)
     if column and rows is not None:
             columnNumber=spectra_df.columns.get_loc(column[0]) 
             i=0
             st.write(len(spectra))
             spectrafor_df = pd.read_csv(spectra[1])
             st.write(spectra)
             st.write(spectrafor_df)
             
