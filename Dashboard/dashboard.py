import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

st.title(" Bike Sharing Dashboard")
st.write(
    """
    Dashboard analisis penggunaan sepeda berdasarkan musim,
    jam, hari kerja, dan kondisi cuaca pada tahun 2011–2012.
    """
)

# =========================================================
# LOAD DATA
# Menggunakan main_data.csv
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "main_data.csv")

main_df = pd.read_csv(file_path)

# Konversi tipe data tanggal
main_df["dteday"] = pd.to_datetime(main_df["dteday"])

# =========================================================
# SIDEBAR FILTER (FITUR INTERAKTIF)
# =========================================================

st.sidebar.header(" Filter Dashboard")

# Filter musim
season_option = st.sidebar.selectbox(
    "Pilih Musim",
    options=["All"] + sorted(main_df["season_desc"].unique().tolist())
)

# Filter tanggal
start_date = st.sidebar.date_input(
    "Tanggal Awal",
    value=main_df["dteday"].min()
)

end_date = st.sidebar.date_input(
    "Tanggal Akhir",
    value=main_df["dteday"].max()
)

# =========================================================
# FILTER DATA
# =========================================================

filtered_df = main_df.copy()

# Filter season
if season_option != "All":
    filtered_df = filtered_df[
        filtered_df["season_desc"] == season_option
    ]

# Filter date
filtered_df = filtered_df[
    (filtered_df["dteday"] >= pd.to_datetime(start_date)) &
    (filtered_df["dteday"] <= pd.to_datetime(end_date))
]

# Kritik penting:
# Jangan biarkan dashboard kosong tanpa handling
if filtered_df.empty:
    st.warning("Data tidak ditemukan untuk filter yang dipilih.")
    st.stop()

# =========================================================
# METRIC UTAMA
# =========================================================

st.subheader(" Ringkasan Data")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Penyewaan",
        int(filtered_df["total_rentals"].sum())
    )

with col2:
    st.metric(
        "Rata-rata Harian",
        round(filtered_df["total_rentals"].mean(), 2)
    )

with col3:
    st.metric(
        "Total Registered User",
        int(filtered_df["registered"].sum())
    )

st.write(
    """
    **Insight Ringkasan:**

    Total penyewaan yang tinggi menunjukkan bahwa layanan
    bike sharing memiliki peran penting sebagai alternatif
    transportasi harian masyarakat.

    Jumlah registered user yang jauh lebih besar dibandingkan
    casual user menunjukkan bahwa mayoritas pengguna merupakan
    pelanggan tetap yang menggunakan layanan ini secara rutin.
    """
)

# =========================================================
# VISUALISASI 1
# MUSIM
# =========================================================

st.subheader("1. Pengaruh Musim terhadap Penyewaan Sepeda")

season_rentals = (
    filtered_df.groupby("season_desc")["total_rentals"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=season_rentals,
    x="season_desc",
    y="total_rentals",
    ax=ax
)

ax.set_title("Rata-rata Penyewaan Berdasarkan Musim")
ax.set_xlabel("Season")
ax.set_ylabel("Average Rentals")

st.pyplot(fig)

st.write(
    """
    **Insight:**

    Musim Summer dan Fall menunjukkan rata-rata jumlah
    penyewaan tertinggi dibandingkan musim lainnya.

    Hal ini menunjukkan bahwa cuaca yang nyaman dan aktivitas
    luar ruangan yang meningkat mendorong penggunaan layanan
    bike sharing secara lebih intensif.
    """
)

# =========================================================
# VISUALISASI 2
# JAM
# =========================================================

st.subheader("2. Pola Penyewaan Berdasarkan Jam")

hourly_rentals = (
    filtered_df.groupby("hr")["total_rentals"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(12, 5))

sns.lineplot(
    data=hourly_rentals,
    x="hr",
    y="total_rentals",
    marker="o",
    ax=ax
)

ax.set_title("Pola Penyewaan Berdasarkan Jam")
ax.set_xlabel("Hour")
ax.set_ylabel("Average Rentals")

st.pyplot(fig)

st.write(
    """
    **Insight:**

    Puncak penyewaan terjadi pada pukul 08.00
    serta pukul 17.00–18.00.

    Pola ini menunjukkan dominasi penggunaan sepeda
    untuk aktivitas commuting seperti berangkat kerja,
    kuliah, dan perjalanan pulang.
    """
)

# =========================================================
# VISUALISASI 3
# HARI KERJA
# =========================================================

st.subheader("3. Hari Kerja vs Akhir Pekan")

workingday_rentals = (
    filtered_df.groupby("workingday_desc")["total_rentals"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    data=workingday_rentals,
    x="workingday_desc",
    y="total_rentals",
    ax=ax
)

ax.set_title("Perbandingan Hari Kerja dan Akhir Pekan")
ax.set_xlabel("Category")
ax.set_ylabel("Average Rentals")

st.pyplot(fig)

st.write(
    """
    **Insight:**

    Hari kerja memiliki jumlah penyewaan lebih tinggi
    dibandingkan akhir pekan.

    Hal ini menunjukkan bahwa layanan bike sharing
    lebih dominan digunakan untuk kebutuhan mobilitas rutin.
    """
)

# =========================================================
# VISUALISASI 4
# CUACA
# =========================================================

st.subheader("4. Pengaruh Cuaca terhadap Penyewaan")

weather_rentals = (
    filtered_df.groupby("weather_desc")["total_rentals"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=weather_rentals,
    x="weather_desc",
    y="total_rentals",
    ax=ax
)

ax.set_title("Pengaruh Kondisi Cuaca terhadap Penyewaan")
ax.set_xlabel("Weather Situation")
ax.set_ylabel("Average Rentals")

plt.xticks(rotation=15)

st.pyplot(fig)

st.write(
    """
    **Insight:**

    Cuaca cerah menghasilkan jumlah penyewaan tertinggi,
    sedangkan cuaca buruk seperti hujan atau salju
    menyebabkan penurunan signifikan.

    Kondisi cuaca menjadi faktor utama dalam keputusan
    pengguna untuk menggunakan layanan bike sharing.
    """
)

# =========================================================
# CONCLUSION
# =========================================================

st.subheader(" Conclusion")

st.write(
    """
    Bike sharing sangat dipengaruhi oleh musim,
    waktu, hari kerja, dan kondisi cuaca.

    Musim Summer dan Fall menjadi periode dengan
    penyewaan tertinggi.

    Puncak penggunaan terjadi pada pagi dan sore hari,
    yang menunjukkan dominasi aktivitas commuting.

    Hari kerja memiliki jumlah rental lebih tinggi
    dibandingkan akhir pekan, sedangkan cuaca cerah
    meningkatkan jumlah penggunaan secara signifikan.

    Informasi ini dapat membantu perusahaan dalam
    pengambilan keputusan operasional dan strategi bisnis.
    """
)