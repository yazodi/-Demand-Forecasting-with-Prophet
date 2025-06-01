import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

st.title("📈 Demand Forecasting App (Prophet ile)")

# Veriyi yükle
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Kullanıcıdan seçim
store = st.selectbox("Mağaza Seç", sorted(df['store'].unique()))
item = st.selectbox("Ürün Seç", sorted(df['item'].unique()))

# Prophet için veri hazırla
filtered = df[(df['store'] == store) & (df['item'] == item)]
dfp = filtered[['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})

# Model kur
model = Prophet()
model.fit(dfp)

# Tahmin
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# Tahmin Grafiği
st.subheader("📊 Tahmin Grafiği")
fig1 = model.plot(forecast)
st.pyplot(fig1)

# Mevsimsellik bileşenleri
st.subheader("🧠 Mevsimsellik & Trend Bileşenleri")
fig2 = model.plot_components(forecast)
st.pyplot(fig2)
