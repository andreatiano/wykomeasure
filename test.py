import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import parse
st.set_page_config(layout="wide")
plotCol, dataCol = st.columns([2,1])
importExp=st.sidebar.expander('Import Option')
importExp.subheader('After import press the button')
verified=importExp.checkbox('Press to start')
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
     if column and rows is not None:
             columnNumber=Data_df.columns.get_loc(column[0])  
             waferdata1=Data_df.iloc[rows[0]:,columnNumber]
             dataset.append(waferdata1)
             result1 = parse.search('CarrierAtPort1.{}.', Data[0].name)
             list.append(f'Wafer_{result1.fixed}')
             for l in range (1,len(Data)):
                Datafor_df = pd.read_csv(Data[l],skiprows=rows[0])
                result = parse.search('CarrierAtPort1.{}.', Data[l].name)
                list.append(f'Wafer_{result.fixed}')
                waferdata=Datafor_df.iloc[:,columnNumber]
                dataset.append(waferdata)
             finalDataset=np.array(dataset)
             finalDataset=finalDataset.reshape(Llen(waferdata1))
             plotData=dataCol.expander('Final Dataset',True)
             plotDataFrame=pd.DataFrame(finalDataset)
             plotData.dataframe(plotDataFrame)
             plotData.download_button('Download current Dataset',plotDataFrame.to_csv().encode('utf-8'),'Measure.csv')
