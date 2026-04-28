# Bike Sharing Dashboard

Proyek ini menganalisis pola penggunaan layanan bike sharing berdasarkan musim, jam, hari kerja, dan kondisi cuaca menggunakan dataset Bike Sharing. Hasil analisis kemudian disajikan dalam dashboard interaktif berbasis Streamlit untuk memudahkan eksplorasi data dan pengambilan insight bisnis.

---

## Dashboard Online

https://dashboardpy-n5ewvfmoee7wkbxwo2srnv.streamlit.app/

---

## Informasi Mahasiswa

- **Nama:** Faza Azka Mahasya
- **Dicoding ID:** faza_azka_m

---

## Pertanyaan Bisnis

1. Bagaimana pengaruh musim terhadap rata-rata jumlah penyewaan sepeda selama tahun 2011–2012?

2. Pada jam berapa rata-rata jumlah penyewaan sepeda mencapai puncaknya dalam satu hari selama periode 2011–2012?

3. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda antara hari kerja dan akhir pekan selama tahun 2011–2012?

4. Bagaimana kondisi cuaca memengaruhi rata-rata jumlah penyewaan sepeda selama periode observasi?

---

## Ringkasan Hasil Analisis

### 1. Pengaruh Musim

Musim Summer dan Fall memiliki rata-rata jumlah penyewaan tertinggi dibandingkan musim lainnya. Hal ini menunjukkan bahwa kondisi cuaca yang nyaman dan meningkatnya aktivitas luar ruangan mendorong penggunaan bike sharing lebih tinggi.

### 2. Pola Penyewaan Berdasarkan Jam

Puncak rata-rata penyewaan terjadi pada pukul 08.00 serta pukul 17.00–18.00. Pola ini menunjukkan bahwa mayoritas pengguna memanfaatkan sepeda untuk aktivitas commuting seperti berangkat kerja, kuliah, dan perjalanan pulang.

### 3. Hari Kerja vs Akhir Pekan

Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan akhir pekan dan hari libur. Hal ini menunjukkan bahwa layanan bike sharing lebih dominan digunakan untuk kebutuhan mobilitas rutin harian.

### 4. Pengaruh Kondisi Cuaca

Cuaca cerah menghasilkan jumlah penyewaan tertinggi, sedangkan cuaca buruk seperti hujan dan salju menyebabkan penurunan jumlah penyewaan secara signifikan.

---

## Struktur Proyek

- `Notebook.ipynb` : notebook utama untuk proses analisis data end-to-end
- `dashboard/dashboard.py` : aplikasi dashboard interaktif menggunakan Streamlit
- `dashboard/main_data.csv` : dataset utama yang digunakan pada dashboard
- `data/day.csv` : dataset penyewaan sepeda harian
- `data/hour.csv` : dataset penyewaan sepeda per jam
- `README.md` : dokumentasi proyek
- `requirements.txt` : daftar library yang digunakan

---

## Menjalankan Proyek di VS Code

1. Buka folder proyek di VS Code.

2. Buka terminal melalui menu:

```bash
Terminal > New Terminal
```

3. Jalankan instalasi dependency:

```bash
pip install -r requirements.txt
```

4. Jalankan dashboard Streamlit dari root project:

```bash
cd dashboard
streamlit run dashboard.py
```
