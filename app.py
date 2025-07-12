import streamlit as st
import streamlit.components.v1 as components  # ini penting untuk HTML custom

st.set_page_config(page_title="Uji Nyala & Titrasi", layout="centered")
st.title("🌈 Uji Nyala & ⚗️ Titrasi Asidi-Basa")

# Menu Sidebar
menu = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Uji Nyala", "Titrasi Asidi-Basa"])

# ------------------- BERANDA -------------------
if menu == "Beranda":
    st.header("👋 Selamat Datang!")
    st.write("""
    Website ini membantu kamu memahami konsep **uji nyala logam** dan **titrasi asam-basa** secara interaktif.
    
    Gunakan menu di sebelah kiri untuk mulai belajar!
    """)

# ------------------- UJI NYALA -------------------
elif menu == "Uji Nyala":
    st.header("🔥 Uji Nyala Logam")

    # Pilihan logam
    logam = st.selectbox("Pilih logam yang diuji:", [
        "Natrium (Na)", "Kalium (K)", "Kalsium (Ca)",
        "Tembaga (Cu)", "Stronsium (Sr)"
    ])

    # Warna nyala per logam (teks)
    warna_teks = {
        "Natrium (Na)": "Kuning terang",
        "Kalium (K)": "Ungu muda",
        "Kalsium (Ca)": "Jingga",
        "Tembaga (Cu)": "Hijau kebiruan",
        "Stronsium (Sr)": "Merah menyala"
    }

    # Warna untuk animasi api
    warna_api = {
        "Natrium (Na)": "gold",
        "Kalium (K)": "violet",
        "Kalsium (Ca)": "orange",
        "Tembaga (Cu)": "turquoise",
        "Stronsium (Sr)": "red"
    }

    # Tampilkan warna nyala
    st.write(f"🔍 Warna nyala: **{warna_teks[logam]}**")

    # Tampilkan animasi api
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

# ------------------- TITRASI -------------------
elif menu == "Titrasi Asidi-Basa":
    st.header("⚗️ Simulasi Titrasi Asam-Basa")

    volume_naoh = st.slider("Volume NaOH ditambahkan (mL)", 0, 50, 25)
    ph = 7 + (volume_naoh - 25) * 0.3  # simulasi sederhana

    st.write(f"📈 pH sekarang: **{ph:.1f}**")

    if ph < 7:
        st.warning("pH asam")
    elif ph == 7:
        st.info("pH netral (titik ekivalen)")
    else:
        st.success("pH basa")

    st.progress(min(max(int((ph/14)*100), 0), 100))
