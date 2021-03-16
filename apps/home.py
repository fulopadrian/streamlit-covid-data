"""
Default streamlit app

Date: 2021-03-16
"""

import streamlit as st
import wget
import os

def downloadData():
    """
    Download owid-covid-data.csv
    """
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

    try:
        result = wget.download(url, "")
    except Exception as e:
        result = 0

    if result != 0:
        os.remove(os.path.basename(url))
        os.rename(result, "owid-covid-data.csv")

    return result

def run():
    st.title("Home")
    st.write("Select an app on the sidebar!")

    st.write("Download the latest dataset from Our World is Data. (https://ourworldindata.org/coronavirus)")
    btn_download = st.button("Download")

    if btn_download:
        with st.spinner("Downloading..."):
            result = downloadData()
        if result != 0:
            st.success("Done!")
        else:
            st.error("Something went wrong!")
