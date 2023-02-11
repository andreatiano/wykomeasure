import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

importExp=st.sidebar.expander('Import Option')
Delimiter= importExp.selectbox('Delimiter:',('\t',';',','))
spectra = importExp.file_uploader("upload file", type={"csv", "txt"})
dataset=[]
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    st.write(spectra_df)
    rows = st.multiselect(
    'select the row of the first measure',spectra_df.index) 
    # spectra_df1=pd.read_csv(spectra,skiprows=rows-1)
    column = st.multiselect(
    'select the correct column',spectra_df.columns.values.tolist())  
    allWafer = importExp.file_uploader("after rows and column selection import all files", type={"csv", "txt"},accept_multiple_files=True)
    if column and rows is not None:
            columnNumber=spectra_df.columns.get_loc(column[0]) 
            for uploaded_file in allWafer:
               spectrafor_df = pd.read_csv(uploaded_file,skiprows=rows-1)
               waferdata=spectrafor_df.iloc[:,columnNumber]
               dataset.append(waferdata)
            plotData=st.expander('fitted data',True)
            plotDataFrame=pd.DataFrame(dataset)
            plotData.dataframe(plotDataFrame) 
