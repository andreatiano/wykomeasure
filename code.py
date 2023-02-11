import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
plotCol, dataCol = st.columns([2,1])
importExp=st.sidebar.expander('Import Option')
Delimiter= importExp.selectbox('Delimiter:',('\t',';',','))
spectra = importExp.file_uploader("upload file", type={"csv", "txt"})
dataset=[]
list=[]
righe=[]
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    rows = st.multiselect(
    'select the row of the first measure',spectra_df.index) 
    column = st.multiselect(
    'select the correct column',spectra_df.columns.values.tolist())  
    st.write(spectra_df)
    if column and rows is not None:
        columnNumber=spectra_df.columns.get_loc(column[0]) 
        allWafer = importExp.file_uploader(st.subheader("After rows and column selection import all files"), type={"csv", "txt"},accept_multiple_files=True)
        if allWafer is not None:  
            i=0
            for uploaded_file in allWafer:
               i=i+1
               spectrafor_df = pd.read_csv(uploaded_file,skiprows=rows[0])
               list.append(f'Wafer_{i}')
               waferdata=spectrafor_df.iloc[:,columnNumber]
               dataset.append(waferdata)
               finalDataset=np.array(dataset)
            plotData=dataCol.expander('Final Dataset')
            plotDataFrame=pd.DataFrame(finalDataset.transpose(),columns=list)
            plotData.dataframe(plotDataFrame)
            plotData.download_button('Download current Dataset',plotDataFrame.to_csv().encode('utf-8'),'Measure.csv')
