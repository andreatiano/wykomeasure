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
st.write(spectra)
if spectra in not None
     spectra_df = pd.read_csv(spectra[1])
     rows = plotCol.multiselect(
     'select the row of the first measure',spectra_df.index) 
     column = plotCol.multiselect(
     'select the correct column',spectra_df.columns.values.tolist())  
     plotCol.write(spectra_df)
     if column and rows is not None:
             columnNumber=spectra_df.columns.get_loc(column[0]) 
             allWafer = importExp.file_uploader("After rows and column selection import all files",accept_multiple_files=True)
             i=0
             for uploaded_file in allWafer:
                i=i+1
                spectrafor_df = pd.read_csv(uploaded_file,skiprows=rows[0])
                list.append(f'Wafer_{i}')
                waferdata=spectrafor_df.iloc[:,columnNumber]
                dataset.append(waferdata)
                finalDataset=np.array(dataset)
             plotData=st.expander('Final Dataset',True)
             plotDataFrame=pd.DataFrame(finalDataset.transpose(),columns=list)
             plotData=dataCol.expander('Final Dataset')
             plotDataFrame=pd.DataFrame(finalDataset.transpose(),columns=list)
             plotData.dataframe(plotDataFrame)
             plotData.download_button('Download current Dataset',plotDataFrame.to_csv().encode('utf-8'),'Measure.csv')
