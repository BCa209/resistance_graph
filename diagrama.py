import matplotlib.pyplot as plt

# Datos experimentales
# R1 = 10 Ω
I_R1 = [0.130, 0.155, 0.329]
V_R1 = [1.331, 1.584, 3.336]

# R2 = 33 Ω
I_R2 = [0.040, 0.063, 0.136]
V_R2 = [1.320, 2.050, 4.423]

# R3 = 100 Ω
I_R3 = [0.014, 0.022, 0.050]
V_R3 = [1.426, 2.289, 5.004]

# Crear figura
plt.figure(figsize=(10, 6))

# Graficar V vs I para cada resistencia
plt.plot(I_R1, V_R1, 'o-', label='R₁ = 10 Ω', color='blue')
plt.plot(I_R2, V_R2, 's-', label='R₂ = 33 Ω', color='green')
plt.plot(I_R3, V_R3, '^-', label='R₃ = 100 Ω', color='red')

# Etiquetas y leyenda
plt.title('Gráfico Voltaje (V) vs Corriente (I) para tres resistencias')
plt.xlabel('Corriente I (A)')
plt.ylabel('Voltaje V (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Mostrar gráfico
plt.show()
