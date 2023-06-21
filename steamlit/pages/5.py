import streamlit as st
import pandas as pd
import altair as alt

# create sample data
data = pd.DataFrame({
    'time': [10, 25, 5, 15, 30, 20, 10, 5, 40, 60],
    'name': ['User1', 'User2', 'User3', 'User4', 'User5',
             'User6', 'User7', 'User8', 'User9', 'User10'],
    'page': ['Suspicious', 'Suspicious', 'Information', 'Suspicious', 'Suspicious',
             'Information', 'Information', 'Suspicious', 'Information', 'Suspicious'],
    'session id': ['session1', 'session1', 'session1', 'session2', 'session2',
                   'session3', 'session3', 'session4', 'session4', 'session5'],
})

# histogram of time spent on suspicious file page
histogram = alt.Chart(data[data['page'] == 'Suspicious']).mark_bar().encode(
    alt.X('time:Q', bin=alt.Bin(step=10), title='Time spent on page'),
    y='count()',
    color=alt.Color('count()', legend=None)
).properties(
    title='Time spent on suspicious file page histogram'
)

# grouped bar chart of time spent on different pages
grouped_bar = alt.Chart(data).mark_bar().encode(
    y='time:Q',
    x=alt.X('page:N', sort=['Suspicious', 'Information'], title='Page'),
    color='session id:N'
).properties(
    title='Time spent on different pages by session'
)

# scatter plot of time spent on suspicious file page vs time spent on information page
scatter = alt.Chart(data).mark_circle().encode(
    x='time:Q',
    y=alt.Y('time:Q', title='Time spent on information page'),
    color='session id:N',
    tooltip=['name', 'time']
).properties(
    title='Time spent on suspicious file page vs time spent on information page'
)

# bar chart of time spent on each page by user
bar_chart = alt.Chart(data).mark_bar().encode(
    y='time:Q',
    x=alt.X('page:N', sort=['Suspicious', 'Information'], title='Page'),
    color='name:N'
).properties(
    title='Time spent on each page by user'
)

# stacked bar chart of time spent on each page by user
stacked_bar = alt.Chart(data).mark_bar().encode(
    y='time:Q',
    x=alt.X('name:N', sort=alt.EncodingSortField(field='time', op='sum', order='descending'), title='User'),
    color=alt.Color('page:N', sort=['Suspicious', 'Information'], title='Page')
).properties(
    title='Time spent on each page by user (stacked bar chart)'
)

# scatter plot of time spent on suspicious file page vs time spent on information page (by session)
scatter_by_session = alt.Chart(data).mark_circle().encode(
    x='time:Q',
    y=alt.Y('time:Q', title='Time spent on information page'),
    color='page:N',
    tooltip=['session id', 'time']
).properties(
    title='Time spent on suspicious file page vs time spent on information page (by session)'
)

# display charts in streamlit app
st.altair_chart(histogram, use_container_width=True)
st.altair_chart(grouped_bar, use_container_width=True)
st.altair_chart(scatter, use_container_width=True)
st.altair_chart(bar_chart, use_container_width=True)
st.altair_chart(stacked_bar, use_container_width=True)
st.altair_chart(scatter_by_session, use_container_width=True)

