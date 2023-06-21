from faker import Faker
import random
import streamlit as st
import pandas as pd

fake = Faker()

# Создание списка пользователей
users = []
for i in range(100):
    users.append(fake.name())

# Создание списка страниц
pages = ['home', 'about', 'contact', 'products', 'services']

# Создание списка сессий
sessions = []
for i in range(100):
    sessions.append(fake.uuid4())

# Создание датасета
data = []
for i in range(1000):
    login = random.choice(users)
    page = random.choice(pages)
    session_id = random.choice(sessions)
    time = fake.date_time_this_year()
    duration = random.randint(1, 600)
    data.append([time, duration, login, session_id, page])

df = pd.DataFrame(data, columns=['time', 'duration', 'login', 'session id', 'page'])

# Перевод длительности секунд в минуты
df['duration'] = df['duration'] / 60
