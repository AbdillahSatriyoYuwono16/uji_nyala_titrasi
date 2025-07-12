import streamlit as st

st.set_page_config(page_title="Uji Nyala & Titrasi", layout="centered")

# Judul utama
st.title("🌈 Uji Nyala & ⚗️ Titrasi Asidi-Basa")

# Sidebar Menu
menu = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Uji Nyala", "Titrasi Asidi-Basa"])

# Isi Halaman
if menu == "Beranda":
    st.header("👋 Selamat Datang!")
    st.write("""
    Website ini membantu kamu memahami konsep **uji nyala logam** dan **titrasi asam-basa** secara interaktif.
    
    Gunakan menu di sebelah kiri untuk mulai belajar!
    """)

elif menu == "Uji Nyala":
    st.header("🔥 Uji Nyala Logam")

    logam = st.selectbox("Pilih logam yang diuji:", ["Natrium (Na)", "Kalium (K)", "Kalsium (Ca)", "Tembaga (Cu)", "Stronsium (Sr)"])

    warna = {
        "Natrium (Na)": "Kuning terang",
        "Kalium (K)": "Ungu muda",
        "Kalsium (Ca)": "Jingga",
        "Tembaga (Cu)": "Hijau kebiruan",
        "Stronsium (Sr)": "Merah menyala"
    }

    gambar = {
        "Natrium (Na)": "https://i.imgur.com/7b1YcAS.jpg",     # api natrium
        "Kalium (K)": "https://i.imgur.com/rRKRYXi.jpg",       # api kalium
        "Kalsium (Ca)": "https://i.imgur.com/pwXG1oi.jpg",     # api kalsium
        "Tembaga (Cu)": "https://i.imgur.com/klMbZYX.jpg",     # api tembaga
        "Stronsium (Sr)": "https://i.imgur.com/WzRbQEn.jpg"    # api stronsium
    }

    st.write(f"🔍 Warna nyala: **{warna[logam]}**")
    st.image(gambar[logam], caption=f"Warna nyala {logam}", use_column_width=True)
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
