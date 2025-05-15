# Bernds_Wattrechner
ermittelt die Wattleistung einer Radtour
nach Eingabe der km-Distanz, den absolvierten Höhenmetern und der Fahrtzeit
mittels Addition des Luft-, Roll- und Steigungswiderstands

hier die Berechnungsformeln:
# Konstanten
cwA = 0.4            # Luftwiderstandsbeiwert x Stirnfläche in m²
rho = 1.225          # Luftdichte in kg/m³
c_r = 0.004          # Rollwiderstandskoeffizient
g = 9.81             # Erdbeschleunigung in m/s²

# Berechnungen
v = (distanz * 1000) / (zeit_min * 60)  # Geschwindigkeit in m/s
P_luft = 0.5 * cwA * rho * (v ** 3)
P_hoehe = gewicht * g * (hoehe / (zeit_min * 60))
P_roll = gewicht * g * c_r * v
P_gesamt = P_luft + P_hoehe + P_roll
