# Dashboard Analisis Data ✨

## Setup Environment - Anaconda

```sh
conda create --name main-ds python=3.10
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```sh
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App

```sh
streamlit run dashboard.py
```

## Dependencies

Berikut adalah dependensi yang digunakan dalam proyek ini, yang telah tercantum dalam `requirements.txt`:

- Babel==2.17.0
- matplotlib==3.10.1
- pandas==2.2.3
- seaborn==0.13.2
- streamlit==1.42.2

## Deskripsi Proyek

Dashboard ini digunakan untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti musim, hari libur, hari kerja, dan kondisi cuaca.

## Struktur Folder

```
├── dashboard/
│   ├── dashboard.py
│   ├── day_data.csv
│   ├── Helper Functions Analysis.py
├── requirements.txt
├── README.md
```

