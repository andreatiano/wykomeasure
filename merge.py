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
if verified:
     Data_df = pd.read_csv(Data[0])
     rows = plotCol.multiselect(
     'select the row of the first measure',Data_df.index)
     Data_df = pd.read_csv(Data[0],,skiprows=rows[0])
     st.write(Data_df) 
     if rows is not None:  
             dataset=Data_df
             result1 = parse.search('CarrierAtPort1.{}_', Data[0].name)
             list=result1.fixed
             dimension=len(dataset)
             list=list*dimension
             for l in range (1,len(Data)):
                Datafor_df = pd.read_csv(Data[l],skiprows=rows[0])
                Datafor_df.columns=Data_df.columns
                dataset=pd.concat([dataset,Datafor_df],axis=0)
                result = parse.search('CarrierAtPort1.{}_', Data[l].name)
                list2=result.fixed
                list2=list2*dimension
                list=list+list2
             dataset['wafer']=list
             #column.append('Wafer')
             #finalDatase=dataset[column]
             index = plotCol.multiselect(
                    'select the index of the pivot table',dataset.columns)  
             col = plotCol.multiselect(
                         'select the column of the pivot table',dataset.columns)  
             value = plotCol.multiselect(
                              'select the values of the pivot tablen',dataset.columns) 
             finaldataset=dataset.pivot_table(index=index, columns=col, values=value)
             plotData=st.expander('Final Dataset',True)
             plotData.table(finaldataset)
             plotData.download_button('Download current Dataset',finaldataset.to_csv(),'Measure.csv')
