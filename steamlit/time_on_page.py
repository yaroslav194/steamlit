import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt

st.set_page_config(
    page_title="Hello",
    page_icon="📊",
)
st.markdown("# User activity")

st.sidebar.success("Select a demo above.")

# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)

# for percent_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(percent_complete + 1, text=progress_text)

df = pd.read_csv('/Users/yaroslav/Documents/steamlit/time_on_page_test_7d_1.csv', delimiter=','). \
    rename(columns={"duration": "Time on page", "Login": "Name"})

#st.data_editor(
#    df,
#    column_config={Time on page/60},
#    hide_index=True,
#)
#chart = (
#    alt.Chart(df)
#    .mark_area(opacity=0.7)
#    .encode(
#        y='Time',
#        x='Name',
#        color="Region:N",
 #   )
#)
#st.altair_chart(chart, use_container_width=True)
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Done!')
#st.snow()
st.line_chart(data=df, x='Time on page', y='Name')
