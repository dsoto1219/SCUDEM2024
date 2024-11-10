from constants import TO_PSI


# Average Mammoth mass (kg): From https://www.britannica.com/animal/woolly-mammoth
M = (5500 + 7300) / 2 
vf = 8.49376
Ekf = 0.5 * M * vf**2

F = Ekf/(a/100)
pressure = F / ((2*b / 100) * (2*c / 100))
pressure_psi = pressure * TO_PSI
print(f"{pressure_psi:,.1f} psi")