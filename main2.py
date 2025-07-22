import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Load dataset
df = pd.read_csv("F:/demodashboard2/Assignment4.csv")

st.title("Products Dashboard")
st.header("Select at least one choice")

# Dropdown for category selection
categories = df['Category'].unique()
selected_categories = st.multiselect("Select Category", options=categories, default=categories)

# Filter data and show charts only if at least one category is selected
if selected_categories:
    filtered_df = df[df['Category'].isin(selected_categories)]

    st.subheader("Filtered Data")
    st.write(filtered_df)

    # Bar Chart
    bar_fig = px.bar(
        filtered_df,
        x='Subcategory',
        y='Sales',
        color='Subcategory',
        title='Bar Plot'
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    # Pie Chart
    pie_fig = px.pie(
        filtered_df,
        names='Subcategory',
        values='Sales',
        title='Pie Chart'
    )
    st.plotly_chart(pie_fig, use_container_width=True)

    # Sunburst Chart
    sun_fig = px.sunburst(
        filtered_df,
        path=['Category', 'Subcategory'],
        values='Sales',
        title='Sunburst Chart'
    )
    st.plotly_chart(sun_fig, use_container_width=True)

else:
    st.warning("Please select at least one category to view the data.")
