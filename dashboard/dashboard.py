import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def plot_season_avg(df):
    """Menampilkan rata-rata jumlah sewa sepeda berdasarkan musim."""
    season_avg = df.groupby(by="season")["cnt"].mean()
    season_avg.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title('Rata-rata Jumlah Sepeda Sewa Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Sepeda Sewa')
    plt.xticks(rotation=0)
    plt.show()

def plot_holiday_avg(df):
    """Menampilkan rata-rata jumlah sewa sepeda berdasarkan hari libur."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='holiday', y='cnt', data=df)
    plt.title('Rata-rata Jumlah Sepeda Sewa Berdasarkan Hari Libur')
    plt.xlabel('Hari Libur (0: Tidak, 1: Ya)')
    plt.ylabel('Rata-rata Jumlah Sepeda Sewa')
    plt.show()

def plot_workingday_avg(df):
    """Menampilkan rata-rata jumlah sewa sepeda berdasarkan hari kerja."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='workingday', y='cnt', data=df)
    plt.title('Rata-rata Jumlah Sepeda Sewa Berdasarkan Hari Kerja')
    plt.xlabel('Hari Kerja (0: Tidak, 1: Ya)')
    plt.ylabel('Rata-rata Jumlah Sepeda Sewa')
    plt.show()

def plot_weather_avg(df):
    """Menampilkan rata-rata jumlah sewa sepeda berdasarkan kondisi cuaca."""
    weather_avg = df.groupby(by="weathersit")["cnt"].mean()
    weather_avg.plot(kind='barh', figsize=(10, 6), color='lightgreen')
    plt.title('Rata-rata Jumlah Sepeda Sewa Berdasarkan Cuaca')
    plt.xlabel('Rata-rata Jumlah Sepeda Sewa')
    plt.ylabel('Kondisi Cuaca')
    plt.show()

def analyze_bike_rentals(df):
    """Menjalankan semua visualisasi analisis data."""
    plot_season_avg(df)
    plot_holiday_avg(df)
    plot_workingday_avg(df)
    plot_weather_avg(df)

# Load cleaned data
all_df = pd.read_csv("dashboard/day_data.csv")

# Ubah kolom tanggal ke format datetime
datetime_columns = ["dteday"]
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Urutkan data berdasarkan tanggal
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(drop=True, inplace=True)

# Filter data (mencari rentang tanggal)
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                 (all_df["dteday"] <= str(end_date))]

# Menyiapkan berbagai dataframe
season_avg = main_df.groupby("season")["cnt"].mean().reset_index()
holiday_avg = main_df.groupby("holiday")["cnt"].mean().reset_index()
workingday_avg = main_df.groupby("workingday")["cnt"].mean().reset_index()
weather_avg = main_df.groupby("weathersit")["cnt"].mean().reset_index()

# **Total Penyewaan Sepeda**
st.header("📊 Dashboard Bike Sharing")
col1, col2 = st.columns(2)

with col1:
    total_rentals = main_df["cnt"].sum()
    st.metric("Total Penyewaan", value=total_rentals)

with col2:
    avg_rentals = int(main_df["cnt"].mean())
    st.metric("Rata-rata Penyewaan Harian", value=avg_rentals)

# **Grafik Rata-rata Penyewaan Berdasarkan Musim**
st.subheader("🔆 Rata-rata Jumlah Sepeda Sewa Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="season", y="cnt", data=season_avg, palette="Blues", ax=ax)
ax.set_title("Rata-rata Jumlah Sepeda Sewa Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Sepeda Sewa")
st.pyplot(fig)

# **Grafik Rata-rata Penyewaan Berdasarkan Hari Libur**
st.subheader("📅 Rata-rata Jumlah Sepeda Sewa Berdasarkan Hari Libur")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="holiday", y="cnt", data=holiday_avg, palette="coolwarm", ax=ax)
ax.set_title("Penyewaan Sepeda pada Hari Libur")
ax.set_xlabel("Hari Libur (0 = Tidak, 1 = Ya)")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

# **Grafik Rata-rata Penyewaan Berdasarkan Hari Kerja**
st.subheader("🏢 Rata-rata Jumlah Sepeda Sewa Berdasarkan Hari Kerja")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="workingday", y="cnt", data=workingday_avg, palette="muted", ax=ax)
ax.set_title("Penyewaan Sepeda pada Hari Kerja")
ax.set_xlabel("Hari Kerja (0 = Tidak, 1 = Ya)")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

# **Grafik Rata-rata Penyewaan Berdasarkan Kondisi Cuaca**
st.subheader("🌦️ Rata-rata Jumlah Sepeda Sewa Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(y="weathersit", x="cnt", data=weather_avg, palette="viridis", ax=ax)
ax.set_title("Penyewaan Sepeda Berdasarkan Cuaca")
ax.set_xlabel("Rata-rata Penyewaan Sepeda")
ax.set_ylabel("Kondisi Cuaca")
st.pyplot(fig)

# **Menampilkan Statistik**
st.subheader("📋 Statistik Deskriptif")
st.write(main_df.describe())

st.caption('Copyright © Dicoding 2023')