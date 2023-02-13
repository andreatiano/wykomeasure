import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide")
plotCol, dataCol = st.columns([2,1])
importExp=st.sidebar.expander('Import Option')
importExp.subheader('After import press the button')
verified=importExp.button('Press to start')
Delimiter= importExp.selectbox('Delimiter:',('\t',';',','))
Data= importExp.file_uploader("upload file",accept_multiple_files=True)

list=[]
dataset=[]
if verified:
     Data_df = pd.read_csv(Data[0])
     rows = plotCol.multiselect(
     'select the row of the first measure',Data_df.index) 
     column = plotCol.multiselect(
     'select the correct column',Data_df.columns.values.tolist())  
     plotCol.write(Data_df) 
     verified=True
     if column and rows is not None:
             verified=True
             columnNumber=Data_df.columns.get_loc(column[0])  
             waferdata1=Data_df.iloc[rows[0]:,columnNumber]
             dataset.append(waferdata1)
             list.append('Wafer_1')
             for l in range (1,len(Data)):
                Datafor_df = pd.read_csv(Data[l],skiprows=rows[0])
                list.append(f'Wafer_{l+1}')
                waferdata=Datafor_df.iloc[:,columnNumber]
                dataset.append(waferdata)
             finalDataset=np.array(dataset)
             plotData=dataCol.expander('Final Dataset',True)
             plotDataFrame=pd.DataFrame(finalDataset.transpose(),columns=list)
             plotData.dataframe(plotDataFrame)
             plotData.download_button('Download current Dataset',plotDataFrame.to_csv().encode('utf-8'),'Measure.csv')
