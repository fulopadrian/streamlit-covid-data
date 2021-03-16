"""
Main entry point of the streamlit application
streamilt run main.py

Date: 2021-03-16
"""

import streamlit as st
from MultiApp import MultiApp

# Importing apps
from apps import home
from apps import owid_covid_data

apps = MultiApp()

# Adding apps to MultiApp
apps.addApp("Home", home.run, "home")
apps.addApp("OWID Covid-19 Data", owid_covid_data.run, "owid_covid_data")

apps.run()
