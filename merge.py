import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
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
     instrument= st.text_input('Instrument name','instrument 1')
     plotData1=st.expander(' Dataset',True)
     if rows is None:
          plotData1.table(Data_df)
          st.subheader('Select the row parameter ')
     if rows is not None:  
             dataset=Data_df.iloc[rows[0]:]
             result1 = parse.search('CarrierAtPort1.{}_', Data[0].name)
             list=result1.fixed
             dimension=len(dataset)
             list=list*dimension
             list3=instrument
           
             for l in range (1,len(Data)):
                Datafor_df = pd.read_csv(Data[l])
                Datafor_df=Datafor_df.iloc[rows[0]:]
                dataset=pd.concat([dataset,Datafor_df],axis=0)
                result = parse.search('CarrierAtPort1.{}_', Data[l].name)
                list2=result.fixed
                list2=list2*dimension
                list4=instrument*dimension
                list=list+list2
             dataset['Wafer']=list
             dataset['Instrument']=list3
             #column.append('Wafer')
             #finalDatase=dataset[column]
             
             plotData1.download_button('Download Dataset',dataset.to_csv(),'Total_measurement.csv')
             index = plotCol.multiselect(
                    'select the index of the pivot table',dataset.columns)  
             col = plotCol.multiselect(
                         'select the column of the pivot table',dataset.columns)  
             value = plotCol.multiselect(
                              'select the values of the pivot tablen',dataset.columns)
             try:
               dataset=dataset.pivot_table(index=index, columns=col, values=value)
               plotData=st.expander('Final Dataset',True)
               plotData.table(dataset)
               plotData.download_button('Download current Dataset',dataset.to_csv(),'Pivot_table.csv')
             except:
               st.subheader('Select the parameter to generate a pivt table')
               
             
         
