from constants import a, b, c, DISTANCE_FROM_HUMAN

# Average Mammoth mass (kg): From https://www.britannica.com/animal/woolly-mammoth
M = (5500 + 7300) / 2 
vf = 8.49376
Ekf = 0.5 * M * vf**2

F = Ekf/DISTANCE_FROM_HUMAN
pressure = F / ((2*b / 100) * (2*c / 100))**2
pressure_psi = pressure * 0.0001450377 # number obtained from https://www.unitconverters.net/pressure/pascal-to-psi.htm
print(f"{pressure:.2E} Pascals, or {pressure_psi:.2E} psi")