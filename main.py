import streamlit as st
from MultiApp import MultiApp

from apps import home
from apps import owid_covid_data

apps = MultiApp()

apps.addApp("Home", home.run, "home")
apps.addApp("OWID Covid-19 Data", owid_covid_data.run, "owid_covid_data")

apps.run()
