import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
plotCol, dataCol = st.columns([2,1])
importExp=st.sidebar.expander('Import Option')
Delimiter= importExp.selectbox('Delimiter:',('\t',';',','))
allWafer = importExp.file_uploader("Import measurement files", type={"csv", "txt"},accept_multiple_files=True)
dataset=[]
list=[]
righe=[]
if spectra is not None:
    layout_df = pd.read_csv(allWafer[1])
    rows = st.multiselect(
    'select the row of the first measure',layout_df.index) 
    column = st.multiselect(
    'select the correct column',layout_df.columns.values.tolist())  
    st.write(layout_df)
    if column and rows is not None:
        columnNumber=layout_df.columns.get_loc(column[0])  
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
