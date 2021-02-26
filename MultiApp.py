import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def addApp(self, title, function, role):
        self.apps.append({"title": title, "function": function, "role": role})

    def run(self):
        st.sidebar.header("Apps")

        app = st.sidebar.selectbox("Select app", self.apps, format_func=lambda app: app['title'])

        app["function"]()
