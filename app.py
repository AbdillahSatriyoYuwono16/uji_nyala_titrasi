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
    st.title("ðŸ”¬ Selamat Datang di Aplikasi Kimia Interaktif")
    st.write("Kelompok 2 - Kelas 1A")
    st.write("Silakan pilih menu di sebelah kiri untuk memulai.")
    st.image("https://cdn.pixabay.com/photo/2020/03/17/03/32/laboratory-4936936_960_720.png", width=400)

# --- Menu UJI NYALA ---
elif menu == "Uji Nyala":
    st.header("ðŸ”¥ Uji Nyala Logam")

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
        "Natrium (Na)": "ðŸ”¬ Elektron natrium tereksitasi dan kembali ke keadaan dasar, memancarkan cahaya kuning di sekitar 589 nm.",
        "Kalium (K)": "ðŸ”¬ Kalium memancarkan warna ungu muda karena transisi elektron pada panjang gelombang sekitar 766 nm.",
        "Kalsium (Ca)": "ðŸ”¬ Warna jingga berasal dari eksitasi elektron kalsium, memancarkan cahaya sekitar 622 nm.",
        "Tembaga (Cu)": "ðŸ”¬ Tembaga menghasilkan warna hijau kebiruan karena elektron memancarkan cahaya sekitar 510â€“520 nm.",
        "Stronsium (Sr)": "ðŸ”¬ Warna merah terang berasal dari transisi elektron stronsium di sekitar 606â€“670 nm."
    }

    if st.button("ðŸ”¬ Mulai Uji Nyala"):
        st.success(f"âœ… Warna nyala: **{warna_teks[logam]}**")
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
    st.header("âš—ï¸ Simulasi Titrasi Asam-Basa")

    st.markdown("""
Titrasi asam-basa adalah metode untuk menentukan konsentrasi suatu larutan asam atau basa dengan menambahkan larutan penitrasi (basa atau asam yang telah diketahui konsentrasinya) hingga tercapai titik ekivalen.

**Rumus dasar:**
> Ma Ã— Va = Mb Ã— Vb
""")

    # Pilihan larutan
    asam = st.selectbox("Pilih jenis asam:", ["HCl", "CHâ‚ƒCOOH"])
    basa = st.selectbox("Pilih jenis basa:", ["NaOH", "KOH"])

    Ma = st.number_input("Konsentrasi Asam (Ma) mol/L", 0.1, 2.0, 1.0, step=0.1)
    Va = st.slider("Volume Asam (Va) mL", 5, 50, 25)
    Mb = st.number_input("Konsentrasi Basa (Mb) mol/L", 0.1, 2.0, 1.0, step=0.1)

    if Ma > 0 and Va > 0 and Mb > 0:
        Vb = (Ma * Va) / Mb
        st.success(f"ðŸŒŸ Volume basa yang dibutuhkan: **{Vb:.2f} mL**")
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

    st.metric("ðŸ“Š pH Simulasi", f"{ph}")

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
    st.header("ðŸ§¾ Klasifikasi Asam dan Basa")

    data = {
        "Nama Zat": [
            "HCl", "Hâ‚‚SOâ‚„", "HNOâ‚ƒ", "CHâ‚ƒCOOH", "Hâ‚‚COâ‚ƒ",
            "NaOH", "KOH", "NHâ‚„OH", "Ba(OH)â‚‚", "Mg(OH)â‚‚"
        ],
        "Jenis": [
            "Asam Kuat", "Asam Kuat", "Asam Kuat", "Asam Lemah", "Asam Lemah",
            "Basa Kuat", "Basa Kuat", "Basa Lemah", "Basa Kuat", "Basa Lemah"
        ]
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.info("ðŸ§  Catatan:\n- Asam kuat terionisasi sempurna dalam air.\n- Asam lemah hanya sebagian.\n- Begitu pula dengan basa kuat/lemah.")

# --- Menu KUIS ---
elif menu == "Kuis Asam-Basa":
    st.header("ðŸ§  Kuis Sederhana: Asam atau Basa?")

    soal = {
        "CHâ‚ƒCOOH": "Asam Lemah",
        "HNOâ‚ƒ": "Asam Kuat",
        "NaOH": "Basa Kuat",
        "NHâ‚„OH": "Basa Lemah",
        "KOH": "Basa Kuat"
    }

    skor = 0
    for zat, jawaban_benar in soal.items():
        pilihan = st.radio(f"Apa jenis dari {zat}?", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"], key=zat)
        if pilihan == jawaban_benar:
            st.success("âœ… Benar")
            skor += 1
        else:
            st.error(f"âŒ Salah. Jawaban: {jawaban_benar}")

    st.markdown("---")
    st.subheader(f"ðŸŽ¯ Skor kamu: {skor} dari {len(soal)}")
