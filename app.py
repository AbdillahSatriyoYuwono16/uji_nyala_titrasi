import streamlit as st
import streamlit.components.v1 as components

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda", "Uji Nyala", "Titrasi Asam Basa"]
)

# --- Menu BERANDA ---
if menu == "Beranda":
    st.title("🔬 Selamat Datang di Aplikasi Kimia Interaktif")
    st.write("Silakan pilih menu di sebelah kiri untuk memulai.")
    st.image("https://cdn.pixabay.com/photo/2020/03/17/03/32/laboratory-4936936_960_720.png", width=400)

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

# --- Menu TITRASI ASAM BASA ---
elif menu == "Titrasi Asam Basa":
    st.header("⚗️ Titrasi Asam-Basa")

    st.markdown("""
Titrasi asam-basa adalah teknik untuk menentukan konsentrasi suatu larutan asam atau basa  
dengan menambahkan larutan penitrasi (basa/asam yang sudah diketahui konsentrasinya) secara bertahap.

Rumus dasar:
> **Ma × Va = Mb × Vb**
""")

    # Pilih asam dan basa
    asam = st.selectbox("Pilih jenis asam:", ["HCl", "CH₃COOH"])
    basa = st.selectbox("Pilih jenis basa:", ["NaOH", "KOH"])

    # Input nilai-nilai
    Ma = st.number_input("Konsentrasi Asam (Ma) mol/L", min_value=0.0, step=0.1)
    Va = st.number_input("Volume Asam (Va) mL", min_value=0.0, step=1.0)
    Mb = st.number_input("Konsentrasi Basa (Mb) mol/L", min_value=0.0, step=0.1)

    if Ma > 0 and Va > 0 and Mb > 0:
        # Hitung volume basa
        Vb = (Ma * Va) / Mb
        st.success(f"🎯 Volume basa yang dibutuhkan: **{Vb:.2f} mL**")
    else:
        st.info("Masukkan semua nilai untuk menghitung volume basa.")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Acid-base_titration_curve.png", caption="Kurva Titrasi Asam-Basa", use_column_width=True)
