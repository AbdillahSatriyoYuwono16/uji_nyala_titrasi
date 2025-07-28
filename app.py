import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.set_page_config(page_title="Aplikasi Kimia Interaktif", layout="centered")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda", "Uji Nyala", "Titrasi Asam Basa", "Klasifikasi Asam-Basa", "Kuis Asam-Basa", "Hitung SD"]
)

# --- Menu BERANDA ---
if menu == "Beranda":
    st.title("🔬 Selamat Datang di ChemSpark | Virtual mini Lab: Flame Test & Titration ")
    st.subheader("🧪 1A Kelompok 2")
    st.write("Selamat datang di aplikasi pembelajaran kimia interaktif berbasis web. Di sini, kamu bisa memahami konsep **Uji Nyala Logam** dan **Titrasi Asam-Basa** melalui simulasi dan visualisasi yang menyenangkan!")

    st.markdown("---")

    # Penjelasan Uji Nyala
    st.subheader("🔥 Apa itu Uji Nyala?")
    st.write("""
    Uji nyala adalah metode identifikasi unsur logam berdasarkan **warna api** yang dihasilkan ketika senyawa logam dibakar.
    Warna yang muncul berasal dari elektron yang tereksitasi dan kembali ke keadaan dasar, memancarkan cahaya dengan panjang gelombang tertentu.
    """)

    st.markdown("---")

    # Penjelasan Titrasi
    st.subheader("⚗️ Apa itu Titrasi Asam-Basa?")
    st.write("""
    Titrasi adalah proses menambahkan larutan penitrasi (basa atau asam) secara bertahap untuk menentukan konsentrasi larutan lain berdasarkan titik **netralisasi** (pH = 7).
    Pada titik ini terjadi reaksi setara antara asam dan basa, ditandai oleh **indikator warna** atau perubahan pH.
    """)

    st.markdown("---")
    st.info("Gunakan menu di sebelah kiri untuk mulai simulasi interaktif.")

# --- Menu UJI NYALA ---
elif menu == "Uji Nyala":
    st.header("🔥 Uji Nyala Logam")

    logam = st.selectbox("Pilih logam yang diuji:", [
        "Natrium (Na)", "Kalium (K)", "Kalsium (Ca)",
        "Tembaga (Cu)", "Stronsium (Sr)", "Barium (Ba)", "Litium (Li)"
    ])

    warna_teks = {
        "Natrium (Na)": "Kuning terang",
        "Kalium (K)": "Ungu muda",
        "Kalsium (Ca)": "Jingga",
        "Tembaga (Cu)": "Hijau kebiruan",
        "Stronsium (Sr)": "Merah menyala",
        "Barium (Ba)": "Hijau pucat",
        "Litium (Li)": "Merah karmin"
    }

    warna_api = {
        "Natrium (Na)": "gold",
        "Kalium (K)": "violet",
        "Kalsium (Ca)": "orange",
        "Tembaga (Cu)": "turquoise",
        "Stronsium (Sr)": "red",
        "Barium (Ba)": "lightgreen",
        "Litium (Li)": "crimson"
    }

    penjelasan = {
        "Natrium (Na)": "🔬 Elektron natrium tereksitasi dan kembali ke keadaan dasar, memancarkan cahaya kuning di sekitar 589 nm.",
        "Kalium (K)": "🔬 Kalium memancarkan warna ungu muda karena transisi elektron pada panjang gelombang sekitar 766 nm.",
        "Kalsium (Ca)": "🔬 Warna jingga berasal dari eksitasi elektron kalsium, memancarkan cahaya sekitar 622 nm.",
        "Tembaga (Cu)": "🔬 Tembaga menghasilkan warna hijau kebiruan karena elektron memancarkan cahaya sekitar 510–520 nm.",
        "Stronsium (Sr)": "🔬 Warna merah terang berasal dari transisi elektron stronsium di sekitar 606–670 nm.",
        "Barium (Ba)": "🔬 Barium memberikan warna hijau pucat saat dibakar, menunjukkan panjang gelombang khas sekitar 524 nm.",
        "Litium (Li)": "🔬 Litium menghasilkan warna merah karmin karena eksitasi elektron pada sekitar 670 nm."
    }

    if st.button("🔬 Mulai Uji Nyala"):
        st.success(f"✅ Warna nyala: **{warna_teks[logam]}**")
        st.info(penjelasan[logam])

        warna_nyala = warna_api[logam]

        components.html(f"""
        <div style="text-align:center">
          <h3 style="color:{warna_nyala}">Simulasi Api: {logam}</h3>
          <div class="flame"></div>
        </div>
        <style>
        .flame {{
          margin: auto;
          width: 80px;
          height: 80px;
          background: radial-gradient(circle, {warna_nyala}, black);
          border-radius: 50%;
          box-shadow: 0 0 60px 30px {warna_nyala};
          animation: pulse 0.6s infinite alternate;
        }}
        @keyframes pulse {{
          from {{ transform: scale(1); opacity: 1; }}
          to {{ transform: scale(1.3); opacity: 0.6; }}
        }}
        </style>
        """, height=300)
    else:
        st.warning("Klik tombol di atas untuk memulai simulasi uji nyala.")

# --- Menu KLASIFIKASI ---
elif menu == "Klasifikasi Asam-Basa":
    st.header("🧾 Klasifikasi Asam dan Basa")

    data = {
        "Nama Zat": [
            "HCl", "H₂SO₄", "HNO₃", "CH₃COOH", "H₂CO₃",
            "NaOH", "KOH", "NH₄OH", "Ba(OH)₂", "Mg(OH)₂",
            "HBr", "HI", "HF", "LiOH", "Ca(OH)₂"
        ],
        "Jenis": [
            "Asam Kuat", "Asam Kuat", "Asam Kuat", "Asam Lemah", "Asam Lemah",
            "Basa Kuat", "Basa Kuat", "Basa Lemah", "Basa Kuat", "Basa Lemah",
            "Asam Kuat", "Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Kuat"
        ]
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.info("🧠 Catatan:\n- Asam kuat terionisasi sempurna dalam air.\n- Asam lemah hanya sebagian.\n- Basa kuat mengion sempurna, sedangkan basa lemah hanya sebagian.")

# --- Menu KUIS ---
elif menu == "Kuis Asam-Basa":
    st.header("🧠 Kuis Interaktif Asam-Basa")

    with st.form("kuis"):
        st.write("### Soal 1: Manakah dari berikut ini yang merupakan asam kuat?")
        jawaban1 = st.radio("", ["CH₃COOH", "HCl", "H₂CO₃"])

        st.write("### Soal 2: Apa yang terjadi pada titik ekuivalen dalam titrasi asam-basa?")
        jawaban2 = st.radio("", ["pH = 7", "Semua basa habis", "Indikator berubah menjadi merah"])

        submit = st.form_submit_button("Submit Jawaban")

    if submit:
        score = 0
        if jawaban1 == "HCl":
            score += 1
        if jawaban2 == "pH = 7":
            score += 1

        st.success(f"Skor kamu: {score}/2")

# --- Menu HITUNG SD ---
elif menu == "Hitung SD":
    st.header("📊 Hitung Standar Deviasi (SD)")

    data_input = st.text_area("Masukkan data angka, pisahkan dengan koma (contoh: 2, 4, 6, 8)")

    if st.button("Hitung SD"):
        try:
            data = [float(i) for i in data_input.split(",")]
            mean = np.mean(data)
            sd = np.std(data, ddof=1)
            st.write(f"Rata-rata (mean): {mean:.2f}")
            st.write(f"Standar Deviasi (SD): {sd:.2f}")
        except:
            st.error("Format input salah. Pastikan angka dipisahkan dengan koma.")
