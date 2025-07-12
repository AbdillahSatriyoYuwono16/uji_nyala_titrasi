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
