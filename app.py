import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Dashboard Absensi Karyawan", layout="wide")

    st.title("Dashboard Absensi Karyawan")
    st.write("Visualisasi data absensi harian karyawan.")

    st.image(
        "image.png",
        use_container_width=True
    )

    data = pd.DataFrame({
        "id": range(1, 26),
        "tanggal": [
            "2025-01-02", "2025-01-02", "2025-01-02",
            "2025-01-03", "2025-01-03", "2025-01-03",
            "2025-01-04", "2025-01-04", "2025-01-04",
            "2025-01-05", "2025-01-05", "2025-01-05",
            "2025-01-06", "2025-01-06", "2025-01-06",
            "2025-01-07", "2025-01-07", "2025-01-07",
            "2025-01-08", "2025-01-08", "2025-01-08",
            "2025-01-09", "2025-01-09", "2025-01-09",
            "2025-01-10"
        ],
        "nama_karyawan": [
            "Andi Pratama", "Siti Rahma", "Bayu Saputra",
            "Ayu Lestari", "Rio Firmansyah", "Dwi Novitasari",
            "Putri Amelia", "Budi Santoso", "Indah Kurnia",
            "Tegar Prakoso", "Yuni Safitri", "Arman Fadli",
            "Riska Amelia", "Adit Nugroho", "Dina Wulandari",
            "Fadil Akbar", "Putra Mahendra", "Sarah Oktaviani",
            "Kevin Saputra", "Larasati Dewi", "Hendra Setiawan",
            "Nadia Salma", "Abdi Pratama", "Salsa Maharani",
            "Reza Firmansyah"
        ],
        "departemen": [
            "Finance", "HRD", "IT",
            "Marketing", "Finance", "HRD",
            "IT", "Marketing", "Finance",
            "HRD", "IT", "Marketing",
            "Finance", "HRD", "IT",
            "Marketing", "Finance", "HRD",
            "IT", "Marketing", "Finance",
            "HRD", "IT", "Marketing",
            "Finance"
        ],
        "jam_masuk": [
            "08:05", "07:55", "08:10",
            "08:00", "08:15", "08:00",
            "07:50", "08:20", "08:00",
            "08:30", "07:55", "08:05",
            "08:00", "08:10", "07:50",
            "08:00", "08:25", "08:00",
            "07:55", "08:40", "08:00",
            "08:05", "07:50", "08:00",
            "08:30"
        ],
        "jam_pulang": [
            "16:30", "16:20", "17:00",
            "16:00", "16:40", "16:10",
            "16:30", "17:10", "16:00",
            "16:50", "16:40", "16:30",
            "16:05", "16:20", "16:10",
            "17:00", "16:40", "16:00",
            "16:50", "17:20", "16:15",
            "16:30", "16:20", "17:10",
            "16:55"
        ],
        "status": [
            "Terlambat", "Hadir", "Terlambat",
            "Hadir", "Terlambat", "Hadir",
            "Hadir", "Terlambat", "Hadir",
            "Terlambat", "Hadir", "Terlambat",
            "Hadir", "Terlambat", "Hadir",
            "Hadir", "Terlambat", "Hadir",
            "Hadir", "Terlambat", "Hadir",
            "Terlambat", "Hadir", "Hadir",
            "Terlambat"
        ]
    })

    data["tanggal"] = pd.to_datetime(data["tanggal"])

    st.subheader("📄 Tabel Data Absensi")
    st.dataframe(data)

    # ================================
    # SIDEBAR PANEL
    # ================================
    st.sidebar.title("Panel Kontrol")
    st.sidebar.write("Gunakan panel ini untuk memilih visualisasi dan filter.")

    pilihan = st.sidebar.selectbox(
        "Pilih Jenis Visualisasi:",
        ["Bar Chart", "Line Chart", "Area Chart", "Pie Chart", "Map Chart"]
    )

    dept_filter = st.sidebar.selectbox(
        "Filter Berdasarkan Departemen:",
        data["departemen"].unique()
    )

    # ================================
    # STATISTIK DASAR
    # ================================
    st.sidebar.subheader("📊 Statistik Status Absensi")
    st.sidebar.write(data["status"].value_counts())

    # ================================
    # VISUALISASI
    # ================================
    st.subheader("📈 Visualisasi Data")

    status_counts = data["status"].value_counts()
    absen_per_tanggal = data.groupby("tanggal")["status"].count()
    dept_count = data["departemen"].value_counts()

    if pilihan == "Bar Chart":
        st.write("### 📊 Bar Chart – Jumlah Status Absensi")
        st.bar_chart(status_counts)

    elif pilihan == "Line Chart":
        st.write("### 📈 Line Chart – Jumlah Kehadiran Per Tanggal")
        st.line_chart(absen_per_tanggal)

    elif pilihan == "Area Chart":
        st.write("### 🟩 Area Chart – Jumlah Karyawan Per Departemen")
        st.area_chart(dept_count)

    elif pilihan == "Pie Chart":
        st.write("### 🥧 Pie Chart – Distribusi Status Absensi")
        fig, ax = plt.subplots()
        ax.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%")
        ax.axis("equal")
        st.pyplot(fig)

    elif pilihan == "Map Chart":
        st.write("### 🗺️ Map Lokasi Departemen")
        lokasi = pd.DataFrame({
            "departemen": ["Finance", "HRD", "IT", "Marketing"],
            "latitude": [-1.255, -1.260, -1.265, -1.270],
            "longitude": [116.825, 116.830, 116.835, 116.840]
        })
        st.map(lokasi, latitude="latitude", longitude="longitude")

    # ================================
    # FILTER TABEL
    # ================================
    st.subheader(f"Data Departemen: {dept_filter}")
    st.dataframe(data[data["departemen"] == dept_filter])


if __name__ == "__main__":
    main()
