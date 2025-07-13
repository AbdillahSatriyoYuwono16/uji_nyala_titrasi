import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Aplikasi Kimia Interaktif", layout="centered")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda", "Uji Nyala", "Titrasi Asam Basa", "Klasifikasi Asam-Basa", "Kuis Asam-Basa"]
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
        "Tembaga (Cu)", "Stronsium (Sr)"
    ])

    warna_teks = {
        "Natrium (Na)": "Kuning terang",
        "Kalium (K)": "Ungu muda",
        "Kalsium (Ca)": "Jingga",
        "Tembaga (Cu)": "Hijau kebiruan",
        "Stronsium (Sr)": "Merah menyala"
    }

    warna_api = {
        "Natrium (Na)": "gold",
        "Kalium (K)": "violet",
        "Kalsium (Ca)": "orange",
        "Tembaga (Cu)": "turquoise",
        "Stronsium (Sr)": "red"
    }

    penjelasan = {
        "Natrium (Na)": "🔬 Elektron natrium tereksitasi dan kembali ke keadaan dasar, memancarkan cahaya kuning di sekitar 589 nm.",
        "Kalium (K)": "🔬 Kalium memancarkan warna ungu muda karena transisi elektron pada panjang gelombang sekitar 766 nm.",
        "Kalsium (Ca)": "🔬 Warna jingga berasal dari eksitasi elektron kalsium, memancarkan cahaya sekitar 622 nm.",
        "Tembaga (Cu)": "🔬 Tembaga menghasilkan warna hijau kebiruan karena elektron memancarkan cahaya sekitar 510–520 nm.",
        "Stronsium (Sr)": "🔬 Warna merah terang berasal dari transisi elektron stronsium di sekitar 606–670 nm."
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

# --- Menu TITRASI ---
elif menu == "Titrasi Asam Basa":
    st.header("⚗️ Simulasi Titrasi Asam-Basa")

    st.markdown("""
Titrasi asam-basa adalah metode untuk menentukan konsentrasi suatu larutan asam atau basa dengan menambahkan larutan penitrasi (basa atau asam yang telah diketahui konsentrasinya) hingga tercapai titik ekivalen.

**Rumus dasar:**
> Ma × Va = Mb × Vb
""")

    # Pilihan larutan
    asam = st.selectbox("Pilih jenis asam:", ["HCl", "CH₃COOH"])
    basa = st.selectbox("Pilih jenis basa:", ["NaOH", "KOH"])

    Ma = st.number_input("Konsentrasi Asam (Ma) mol/L", 0.1, 2.0, 1.0, step=0.1)
    Va = st.slider("Volume Asam (Va) mL", 5, 50, 25)
    Mb = st.number_input("Konsentrasi Basa (Mb) mol/L", 0.1, 2.0, 1.0, step=0.1)

    if Ma > 0 and Va > 0 and Mb > 0:
        Vb = (Ma * Va) / Mb
        st.success(f"🌟 Volume basa yang dibutuhkan: **{Vb:.2f} mL**")
    else:
        st.warning("Masukkan semua nilai terlebih dahulu.")

    volume_basa = st.slider("Simulasi penambahan basa (mL)", 0, 50, 0)

    # Perhitungan pH (sederhana)
    delta = volume_basa - Vb
    if delta < 0:
        ph = 3 + (volume_basa / Vb) * 4
    elif delta == 0:
        ph = 7
    else:
        ph = 7 + min(delta * 0.5, 7)
    ph = round(ph, 1)

    st.metric("📊 pH Simulasi", f"{ph}")

    if ph < 7:
        warna = "red"
        keterangan = "Larutan bersifat asam"
    elif ph == 7:
        warna = "blue"
        keterangan = "Larutan netral (titik ekivalen)"
    else:
        warna = "green"
        keterangan = "Larutan bersifat basa"

    components.html(f"""
    <div style="text-align:center; margin-top:20px;">
        <div style="
            width:100px;
            height:100px;
            margin:auto;
            border-radius:50%;
            background:{warna};
            box-shadow:0 0 40px 20px {warna};
            animation:pulse 1s infinite alternate;
        "></div>
        <p style="font-size:20px; color:{warna}; font-weight:bold; margin-top:10px;">{keterangan}</p>
    </div>
    <style>
    @keyframes pulse {{
        from {{ transform: scale(1); opacity: 1; }}
        to {{ transform: scale(1.1); opacity: 0.7; }}
    }}
    </style>
    """, height=200)

    ketinggian = int((volume_basa / 50) * 100)
    components.html(f"""
    <div style="display: flex; justify-content: center; margin-top: 20px;">
      <div style="
        position: relative;
        width: 40px;
        height: 300px;
        background: #ccc;
        border-radius: 10px;
        box-shadow: inset 0 0 5px #888;
        overflow: hidden;
      ">
        <div style="
          position: absolute;
          bottom: 0;
          width: 100%;
          height: {ketinggian}%;
          background: linear-gradient(to top, #00f2ff, #8bfaff);
          transition: height 0.5s;
        "></div>
        <div style="
          position: absolute;
          left: 100%;
          top: 0;
          height: 100%;
          width: 20px;
          font-size: 10px;
          color: #000;
        ">
          <div style="position:absolute; top:0;">50</div>
          <div style="position:absolute; top:25%;">37</div>
          <div style="position:absolute; top:50%;">25</div>
          <div style="position:absolute; top:75%;">12</div>
          <div style="position:absolute; bottom:0;">0</div>
        </div>
      </div>
    </div>
    """, height=350)

    st.progress(min(int((ph / 14) * 100), 100))

# --- Menu KLASIFIKASI ---
elif menu == "Klasifikasi Asam-Basa":
    st.header("🧾 Klasifikasi Asam dan Basa")

    data = {
        "Nama Zat": [
            "HCl", "H₂SO₄", "HNO₃", "CH₃COOH", "H₂CO₃",
            "NaOH", "KOH", "NH₄OH", "Ba(OH)₂", "Mg(OH)₂"
        ],
        "Jenis": [
            "Asam Kuat", "Asam Kuat", "Asam Kuat", "Asam Lemah", "Asam Lemah",
            "Basa Kuat", "Basa Kuat", "Basa Lemah", "Basa Kuat", "Basa Lemah"
        ]
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.info("🧠 Catatan:\n- Asam kuat terionisasi sempurna dalam air.\n- Asam lemah hanya sebagian.\n- Begitu pula dengan basa kuat/lemah.")

# --- Menu KUIS ---
elif menu == "Kuis Asam-Basa":
    st.header("🧠 Kuis: Asam atau Basa?")
    st.write("Pilih jenis senyawa berikut, lalu klik 'Periksa Jawaban' untuk mengetahui hasilnya.")

    soal = {
        "CH₃COOH": "Asam Lemah",
        "HNO₃": "Asam Kuat",
        "NaOH": "Basa Kuat",
        "NH₄OH": "Basa Lemah",
        "KOH": "Basa Kuat"
    }

    jawaban_user = {}
    skor = 0

    with st.form("kuis_form"):
        for zat in soal:
            pilihan = st.radio(f"Apa jenis dari {zat}?", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"], key=zat)
            jawaban_user[zat] = pilihan

        submitted = st.form_submit_button("Periksa Jawaban")

    if submitted:
        for zat in soal:
            if jawaban_user[zat] == soal[zat]:
                st.success(f"✅ {zat} → Benar!")
                skor += 1
            else:
                st.error(f"❌ {zat} → Salah. Jawaban benar: {soal[zat]}")
        
        st.markdown("---")
        st.subheader(f"🎯 Skor akhir kamu: {skor} dari {len(soal)}")
