import streamlit as st
from df_generator import df
import altair as alt

st.markdown("# График активности пользователей")
st.write(
    """"""
)
grouped_data = df.groupby('login').size().reset_index(name='count')
st.bar_chart(grouped_data, x='login', y='count')

st.markdown("# График распределения времени нахождения пользователя на странице по пользователям")
st.write(
    """Кто из пользователей проводит на сайте больше всего времени, а также показывает, 
    есть ли пользователи, которые быстро покидают сайт. Также график может помочь определить, на каких страницах 
    сайта пользователи проводят больше всего времени."""
)
st.bar_chart(df.groupby('login')['duration'].sum())

st.markdown("# График распределения времени нахождения пользователя на странице по идентификаторам сессий")
st.write(
    """Позволяет выявить наиболее активных пользователей и/или наиболее интересные для них страницы. 
    Также можно определить, как долго пользователи обычно находятся на страницах 
    и выявить возможные проблемы с загрузкой страниц или контентом."""
)
st.bar_chart(df.groupby('session id')['duration'].sum())

st.markdown("# График количества посещений страницы по пользователям")
st.write(
    """Позволяет определить, какие пользователи наиболее активно используют сайт и какие страницы 
    наиболее популярны среди пользователей."""
)
st.bar_chart(df.groupby('login')['page'].count())

st.markdown("# График количества посещений страницы по идентификаторам сессий")
st.write(
    """"""
)
st.bar_chart(df.groupby('session id')['page'].count())

st.markdown("# График перехода с")
st.write(
    """Позволяет определить, какие страницы наиболее популярны у пользователей и какой контент на этих страницах 
    наиболее интересен. Эта информация может быть полезна для оптимизации сайта и улучшения пользовательского опыта."""
)
