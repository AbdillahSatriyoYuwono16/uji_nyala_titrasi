import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt

# Menu sidebar
menu = st.sidebar.selectbox(
    "📚 Pilih menu",
    ["Beranda", "Uji Nyala", "Titrasi Asam Basa"]
)

# ============================
# 🔹 BERANDA
# ============================
if menu == "Beranda":
    st.title("🔬 Aplikasi Kimia Interaktif")
    st.write("Selamat datang! Gunakan menu di samping untuk mulai belajar.")
    st.image("https://cdn.pixabay.com/photo/2020/03/17/03/32/laboratory-4936936_960_720.png", width=400)

# ============================
# 🔥 UJI NYALA LOGAM
# ============================
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

# ============================
# ⚗️ TITRASI ASAM BASA
# ============================
elif menu == "Titrasi Asam Basa":
    st.header("⚗️ Titrasi Asam Basa")

    st.markdown("""
Titrasi asam-basa adalah metode untuk menentukan konsentrasi asam atau basa  
dengan meneteskan larutan lawannya hingga titik ekivalen tercapai.

**Rumus utama:**
> Ma × Va = Mb × Vb
""")

    asam = st.selectbox("Pilih jenis asam:", ["HCl", "CH₃COOH"])
    basa = st.selectbox("Pilih jenis basa:", ["NaOH", "KOH"])
    Ma = st.number_input("Konsentrasi Asam (Ma) mol/L", min_value=0.0, step=0.1)
    Va = st.number_input("Volume Asam (Va) mL", min_value=0.0, step=1.0)
    Mb = st.number_input("Konsentrasi Basa (Mb) mol/L", min_value=0.0, step=0.1)

    if Ma > 0 and Va > 0 and Mb > 0:
        Vb = (Ma * Va) / Mb
        st.success(f"🎯 Volume basa yang dibutuhkan: **{Vb:.2f} mL**")
    else:
        st.info("Masukkan semua nilai untuk menghitung volume basa.")

    # ============================
    # 📈 SIMULASI KURVA TITRASI
    # ============================
    st.subheader("📈 Simulasi Kurva Titrasi")

    tipe_titrasi = st.selectbox("Pilih jenis titrasi:", [
        "Asam kuat + Basa kuat",
        "Asam lemah + Basa kuat"
    ])

    Ma_sim = st.number_input("Konsentrasi Asam (mol/L)", 0.1, 2.0, 0.1, key="Ma_sim")
    Va_sim = st.number_input("Volume Asam (mL)", 10.0, 100.0, 25.0, key="Va_sim")
    Mb_sim = st.number_input("Konsentrasi Basa (mol/L)", 0.1, 2.0, 0.1, key="Mb_sim")

    if st.button("🔬 Tampilkan Simulasi"):
        Vb_vals = np.linspace(0.1, Va_sim * 2, 200)
        pH_vals = []
        Ka = 1.8e-5  # untuk CH3COOH (asam lemah)

        for Vb in Vb_vals:
            n_asam = Ma_sim * Va_sim / 1000
            n_basa = Mb_sim * Vb / 1000

            if tipe_titrasi == "Asam kuat + Basa kuat":
                if n_basa < n_asam:
                    H = (n_asam - n_basa) / (Va_sim + Vb) * 1000
                    pH = -np.log10(H)
                elif n_basa == n_asam:
                    pH = 7
                else:
                    OH = (n_basa - n_asam) / (Va_sim + Vb) * 1000
                    pOH = -np.log10(OH)
                    pH = 14 - pOH

            elif tipe_titrasi == "Asam lemah + Basa kuat":
                if n_basa < n_asam:
                    HA = n_asam - n_basa
                    A_ = n_basa
                    H = Ka * (HA / A_)
                    pH = -np.log10(H)
                elif n_basa == n_asam:
                    A_ = n_asam
                    OH = np.sqrt(1e-14 / A_)
                    pOH = -np.log10(OH)
                    pH = 14 - pOH
                else:
                    OH = (n_basa - n_asam) / (Va_sim + Vb) * 1000
                    pOH = -np.log10(OH)
                    pH = 14 - pOH

            pH_vals.append(pH)

        fig, ax = plt.subplots()
        ax.plot(Vb_vals, pH_vals, color='green')
        ax.set_title(f"Kurva Titrasi: {tipe_titrasi}")
        ax.set_xlabel("Volume Basa (mL)")
        ax.set_ylabel("pH")
        ax.grid(True)
        st.pyplot(fig)


