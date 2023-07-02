import numpy as np
import pandas as pd
import streamlit as st
import openpyxl
import odf
from io import BytesIO


uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

chosen = st.radio(
        'Select the file format you want to convert',
        ("CSV", "JSON", "Excel")
        
)

def convert_csv(df):
    return df.to_csv().encode('utf-8')

def convert_excel(df):
    df.to_excel("~/Downloads/converted.ods")

def convert_json(df):
    return df.to_json().encode('utf-8')


def convert(data):
    if (chosen == "Excel"):
        if st.button('Download file'):
            convert_excel(data)
            st.write('File saved to Downloads')

    elif (chosen == "JSON"):
        dosya = convert_json(data)
        st.download_button(
            label="Download file",
            data=dosya,
            file_name="converted.json",
            mime="text/json"
        )

    else:
        dosya = convert_csv(data)
        st.download_button(
            label="Download file",
            data=dosya,
            file_name="converted.csv",
            mime="text/csv"
        )

if (uploaded_files != []):
    for uploaded_file in uploaded_files:
        if (uploaded_file.name.endswith(".csv")):
            data = pd.read_csv(uploaded_file.name)
            convert(data)

        elif (uploaded_file.name.endswith(".json")):
            data = pd.read_json(uploaded_file.name)
            convert(data)
        
        elif (uploaded_file.name.endswith(".xlsx") or uploaded_file.name.endswith(".xls") or uploaded_file.name.endswith(".ods")):
            data = pd.read_excel(uploaded_file.name)
            convert(data)
        
        else:
            st.error('File format not allow')
            break