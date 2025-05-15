# Datei: app.py
import streamlit as st
from PIL import Image
import math

# Bild laden
image_path = "bernd.jpg"  # Bild im selben Ordner wie das Skript
image = Image.open(image_path)

# Layout anpassen: Bild rechts oben
col1, col2 = st.columns([4, 1])
with col1:
    st.title("🚴‍♂️ Bernds Wattrechner")
with col2:
    st.image(image, width=80)

st.markdown("###")

# Eingabefelder
gewicht = st.number_input("Systemgewicht [kg]", value=82.0, min_value=30.0, max_value=200.0)
distanz = st.number_input("Distanz [km]", value=27.22, min_value=0.1)
hoehe = st.number_input("Höhenunterschied [m]", value=230.0, min_value=0.0)
zeit_min = st.number_input("Fahrtzeit [min]", value=52.7, min_value=1.0)

# Konstanten
cwA = 0.28
rho = 1.2
c_rr = 0.005
g = 9.81

# Berechnung
strecke_m = distanz * 1000
zeit_s = zeit_min * 60
v = strecke_m / zeit_s

P_luft = 0.5 * rho * cwA * v**3
P_roll = gewicht * g * c_rr * v
P_hoehe = (gewicht * g * hoehe) / zeit_s
P_gesamt = P_luft + P_roll + P_hoehe

# Ergebnis anzeigen
st.markdown("---")
st.metric("Gesamtleistung", f"{P_gesamt:.1f} Watt")
st.caption("Berechnet aus Luft-, Roll- und Steigungswiderstand.")
st.latex(r"P_{\text{gesamt}} = \frac{1}{2} \cdot \rho \cdot C_wA \cdot v^3 + m \cdot g \cdot C_{rr} \cdot v + \frac{m \cdot g \cdot h}{t}")
st.latex(f"P_{{\\text{{gesamt}}}} = \\frac{{1}}{2} \\cdot {rho} \\cdot {cwA} \\cdot ({v:.2f})^3 + {gewicht} \\cdot {g} \\cdot {c_rr} \\cdot ({v:.2f}) + \\frac{{{gewicht} \\cdot {g} \\cdot {hoehe}}}{{{zeit_s:.2f}}} = {P_gesamt:.1f}~\\text{{Watt}}")
