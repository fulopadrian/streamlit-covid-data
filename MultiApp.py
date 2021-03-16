"""
A class to organize multiple streamlit app into a single one

Date: 2021-03-16
"""

import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def addApp(self, title, function, role):
        self.apps.append({"title": title, "function": function, "role": role})

    def run(self):
        st.sidebar.header("Apps")

        # Creates a selection box on the sidebar where the apps can be selected
        app = st.sidebar.selectbox("Select app", self.apps, format_func=lambda app: app['title'])

        app["function"]()
