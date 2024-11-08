import numpy as np


"""
CONSTANTS
Variables that we do not plan to change.
"""
C_d = 0.5 # Air Drag coefficient/constant, unitless
# velocities, (x, y) pairs resp. (m/s)
rho = 1.225 # air density (kg/m^3)
g = 9.80665 # gravitational constant (m/s^2)


"""
INITIAL CONDITIONS
Things that stay constant throughout the scripts, 
but we can change beforehand.
"""
# Spear metrics
m = 0.5 # spear's mass (kg)
spear_length: float = 1 # spear's length (m)
# See "Shape of Spear.docx" to see conceptual idea of a, b, and c
# all measured in cm
a = 4
b = 1
c = 1

THETA: float = np.radians(45) # angle of the thrown spear
vi: tuple = (15*np.cos(THETA), 15*np.sin(THETA))
threshold: float = 3.447379e+6
# All distances (including height and width) measured in m
HUMAN_HEIGHT = 1.8
MAMMOTH_HEIGHT = 3.5
MAMMOTH_WIDTH = MAMMOTH_HEIGHT * 1.25
DISTANCE_FROM_HUMAN = 20