import streamlit as st
import streamlit.components.v1 as components

# Buat menu di sidebar
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda", "Uji Nyala", "Titrasi Asam Basa"]
)

# Menu Beranda
if menu == "Beranda":
    st.title("🔬 Selamat Datang di Aplikasi Kimia Interaktif")
    st.write("Silakan pilih menu di sebelah kiri untuk memulai.")

# Menu Uji Nyala
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

# Menu Titrasi (opsional kamu isi nanti)
elif menu == "Titrasi Asam Basa":
    st.header("⚗️ Titrasi Asam Basa")
    st.write("Penjelasan tentang titrasi akan ditambahkan di sini.")

