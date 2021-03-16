"""
The Our World In Data COVID-19 dataset visualisation app.

Date: 2021-03-16
"""

import streamlit as st
import pandas as pd

def loadData():
    """
    Loads the data from the csv and drops the unused columns
    """
    df = pd.read_csv("owid-covid-data.csv", sep=",", parse_dates=["date"], na_values=[""])
    df.set_index("date", inplace=True)

    df.drop(["iso_code", "continent", "total_cases", "new_cases_smoothed", "total_deaths", "new_deaths_smoothed", "total_cases_per_million", "new_cases_per_million", "new_cases_smoothed_per_million", "total_deaths_per_million", "new_deaths_per_million", "new_deaths_smoothed_per_million", "reproduction_rate", "icu_patients_per_million", "hosp_patients_per_million", "weekly_icu_admissions", "weekly_icu_admissions_per_million", "weekly_hosp_admissions", "weekly_hosp_admissions_per_million", "total_tests", "total_tests_per_thousand", "new_tests_per_thousand", "new_tests_smoothed", "new_tests_smoothed_per_thousand", "positive_rate", "tests_per_case", "tests_units", "total_vaccinations", "people_vaccinated", "people_fully_vaccinated", "new_vaccinations_smoothed", "total_vaccinations_per_hundred", "people_vaccinated_per_hundred", "people_fully_vaccinated_per_hundred", "new_vaccinations_smoothed_per_million", "stringency_index", "population", "population_density", "median_age", "aged_65_older", "aged_70_older", "gdp_per_capita", "extreme_poverty", "cardiovasc_death_rate", "diabetes_prevalence", "female_smokers", "male_smokers", "handwashing_facilities", "hospital_beds_per_thousand", "life_expectancy", "human_development_index"], axis=1, inplace=True)

    return df

def linePlot(df, options_countries, options_data):
    """
    Creates a default streamlit line charts
    """
    data_by_country = df[df["location"] == options_countries]
    data = data_by_country[options_data]

    st.title(options_countries)
    st.line_chart(data=data)

def run():
    data = loadData()
    items_countries = list(data["location"].unique())
    items_data = list(data.columns.values)
    items_data.remove("location")

    options_countries = st.sidebar.selectbox("Countries", items_countries)
    options_data = st.sidebar.multiselect("Options", items_data, default="new_deaths")

    linePlot(data, options_countries, options_data)

    st.write("Source: https://ourworldindata.org/coronavirus")
