import streamlit as st
import pandas as pd
import altair as alt
from df_generator import df


# Отбираем данные только для страницы home
home_df = df[df['page'] == 'home']

# Группируем данные по страницам
grouped_df = df.groupby(['page', 'session id']).count()['duration'].reset_index()
grouped_df = grouped_df[grouped_df['page'] != 'home']
grouped_df = grouped_df.groupby('page').count()['session id'].reset_index()
st.markdown("# График перехода со страницы home")
st.write(
    """Позволяет определить, какие страницы наиболее популярны у пользователей и какой контент на этих страницах 
    наиболее интересен. Эта информация может быть полезна для оптимизации сайта и улучшения пользовательского опыта."""
)
# Строим график
chart = alt.Chart(grouped_df).mark_bar().encode(
    x='page',
    y='session id'
)

st.altair_chart(chart, use_container_width=True)
