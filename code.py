import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

importExp=st.sidebar.expander('Import Option')
Delimiter= importExp.selectbox('Delimiter:',('\t',';',','))
spectra = importExp.file_uploader("upload file", type={"csv", "txt"})
dataset=[]
list=[]
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    st.write(spectra_df)
    rows = st.multiselect(
    'select the row of the first measure',spectra_df.index) 
    column = st.multiselect(
    'select the correct column',spectra_df.columns.values.tolist())  
    if column and rows is not None:
        columnNumber=spectra_df.columns.get_loc(column[0]) 
        allWafer = importExp.file_uploader("after rows and column selection import all files", type={"csv", "txt"},accept_multiple_files=True)
        if allWafer is not None:  
            i=0
            for uploaded_file in allWafer:
               i++
               spectrafor_df = pd.read_csv(uploaded_file,skiprows=rows[0])
               list.append(f'Wafer_{i}')
               waferdata=spectrafor_df.iloc[:,columnNumber]
               dataset.append(waferdata)
               finalDataset=np.array(dataset)
            plotData=st.expander('fitted data',True)
            plotDataFrame=pd.DataFrame(finalDataset.transpose(),columns=list)
            plotData.dataframe(plotDataFrame) 
