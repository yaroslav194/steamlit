import streamlit as st
import pandas as pd
import altair as alt

# create sample data
data = pd.DataFrame({
    'time': [10, 25, 5, 15, 30, 20, 10, 5, 40, 60],
    'name': ['User1', 'User2', 'User3', 'User4', 'User5',
             'User6', 'User7', 'User8', 'User9', 'User10']
})

# histogram of time spent on suspicious file page
histogram = alt.Chart(data).mark_bar().encode(
    alt.X('time:Q', bin=alt.Bin(step=10), title='Time spent on page'),
    y='count()',
    color=alt.Color('count()', legend=None)
).properties(
    title='Time spent on suspicious file page histogram'
)

# grouped bar chart of time spent on different pages
grouped_bar = alt.Chart(data).mark_bar().encode(
    y='time:Q',
    x='name:N',
    color='name:N'
).properties(
    title='Time spent on different pages by user'
)

# scatter plot of time spent on suspicious file page vs time spent on information page
scatter = alt.Chart(data).mark_circle().encode(
    x='time:Q',
    y='time:Q',
    color='name:N',
    tooltip=['name', 'time']
).properties(
    title='Time spent on suspicious file page vs time spent on information page'
)

# display charts in streamlit app
st.altair_chart(histogram, use_container_width=True)
st.altair_chart(grouped_bar, use_container_width=True)
st.altair_chart(scatter, use_container_width=True)
