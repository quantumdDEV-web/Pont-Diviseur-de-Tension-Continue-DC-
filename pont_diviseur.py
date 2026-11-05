import numpy as np
import matplotlib.pyplot as plt

# ---------- Exercice 2.1 : DC ----------
VCC = 12.0
R1 = 2200.0
R2 = 4700.0

I = VCC / (R1 + R2)            # A
V_R2 = VCC * R2 / (R1 + R2)    # V

print("=== Exercice 2.1 (DC) ===")
print(f"V_R2 = {V_R2:.2f} V")
print(f"I    = {I*1000:.3f} mA")


# Relative error helper (for the Tableau 1 columns)
def ecart(theorique, mesure):
    return abs(mesure - theorique) / theorique * 100


# Example: put your simulator / bench readings here
V_R2_sim = 8.17
I_sim_mA = 1.74
print(f"Ecart V_R2 : {ecart(V_R2, V_R2_sim):.2f} %")
print(f"Ecart I    : {ecart(I*1000, I_sim_mA):.2f} %")

# ---------- Exercice 2.2 : AC ----------
f = 1000.0          # Hz
Vpp = 10.0          # V
Vmax = Vpp / 2      # 5 V
T = 1 / f           # s

Vrms_in = Vmax / np.sqrt(2)
Vmax_out = Vmax * R2 / (R1 + R2)
Vpp_out = 2 * Vmax_out
Vrms_out = Vmax_out / np.sqrt(2)

print("\n=== Exercice 2.2 (AC) ===")
print(f"T = {T*1000:.2f} ms, f = {f:.0f} Hz")
print(f"Vpp1 = {Vpp:.2f} V, Vrms1 = {Vrms_in:.2f} V")
print(f"Vpp2 = {Vpp_out:.2f} V, Vrms2 = {Vrms_out:.2f} V")

# Plot Vin and Vout over 3 periods (like the LTspice 3 ms run)
t = np.linspace(0, 3 * T, 1000)
vin = Vmax * np.sin(2 * np.pi * f * t)
vout = vin * R2 / (R1 + R2)

plt.figure(figsize=(8, 4))
plt.plot(t * 1000, vin, label="Vin (CH1)")
plt.plot(t * 1000, vout, label="Vout aux bornes de R2 (CH2)")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.title("Figure 1 : Vin et Vout du pont diviseur (1 kHz)")
plt.grid(True)
plt.legend()
plt.savefig("oscillogramme.png", dpi=150)
plt.show()
