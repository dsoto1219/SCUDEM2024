import matplotlib.pyplot as plt
import numpy as np
from horizontal_cross_section import cayley_menger_area_3points
from vertical_cross_area import cayley_menger_area_4points


### Constants ###
C_d = 0.5 # Drag coefficient/constant, unitless
# velocities, (x, y) pairs resp. (m/s)
rho = 1.225 # air density (kg/m^3)
g = 9.80665 # gravitational constant (m/s^2)


### Initial conditions ###
THETA: float = np.radians(45) # angle of the thrown spear
vi: tuple = (15*np.cos(THETA), 15*np.sin(THETA))
threshold: float = 1
# All distances (including height and width) measured in m
HUMAN_HEIGHT = 1.8
MAMMOTH_HEIGHT = 3.5
MAMMOTH_WIDTH = MAMMOTH_HEIGHT * 1.25
DISTANCE_FROM_HUMAN = 20
# Spear metrics
m = 0.5 # spear's mass (kg)
spear_length: float = 1 # spear's length (m)
# All metrics in cm
# See "Shape of Spear.docx" to see conceptual idea of a, b, and c
METRICS = {
    "a" : 4, # length
    "b" : 1, # height / 2
    "c" : 1, # depth / 2
}
# Dividing by 10000, since each area is in cm^2 but we want m^2
Ax = cayley_menger_area_4points(*METRICS.values()) / 10000
Ay = cayley_menger_area_3points(METRICS["a"], METRICS["c"]) / 10000

def trajectory(vi: tuple, dt=0.01) -> tuple[list[float], list[float]]:
    """
    Returns list of x, y positions that traces the path of the thrown spear.
    """
    global HUMAN_HEIGHT, MAMMOTH_HEIGHT

    v = [vi]
    # The spear should pass the y-position of the mammoth once before the while loop
    # ends
    is_second_pass: bool = False
    # lists of x and y positions
    s_x = [0]
    s_y = [HUMAN_HEIGHT]

    while (s_y[-1] >= MAMMOTH_HEIGHT) or (not is_second_pass):
        # update Fdx and Fdy on each iteration
        Fdx = 0.5 * C_d * v[-1][0]**2 * rho * Ax
        Fdy = 0.5 * C_d * v[-1][1]**2 * rho * Ay + m * g

        v.append(
            (v[-1][0] - Fdx/m * dt, 
             v[-1][1] - Fdy/m * dt))
        
        s_x.append(s_x[-1] + v[-1][0] * dt)
        s_y.append(s_y[-1] + v[-1][1] * dt)

        if s_y[-1] >= MAMMOTH_HEIGHT:
            is_second_pass = True

    return s_x, s_y


if __name__ == "__main__":
    s_x, s_y = trajectory(vi)
    plt.plot(s_x, s_y)
    plt.xlim(0)
    plt.xlabel('Horizontal position')
    plt.ylim(0)
    plt.ylabel('Vertical position')
    plt.title("Position of spear after being thrown at Mammoth")
    plt.axhline(MAMMOTH_HEIGHT, color='r')
    plt.show()