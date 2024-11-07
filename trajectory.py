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
# See "Shape of Spear.docx" to see conceptual idea of a, b, and c
# all measured in cm
a = 4
b = 1
c = 1
# Horizontal and vertical Cross-section areas (cm)
# Dividing by 10000 since each area is in cm^2 but we want m^2
Ax = cayley_menger_area_4points(a, b, c) / 10000
Ay = cayley_menger_area_3points(a, c) / 10000

def spear_trajectory(initial_velocity: tuple, dt=0.01) -> tuple[list[float], list[float]]:
    """
    Returns list of x, y positions that traces the path of the thrown spear.
    """
    global HUMAN_HEIGHT, MAMMOTH_HEIGHT

    v_x = initial_velocity[0]
    v_y = initial_velocity[1]
    # The spear should pass the y-position of the mammoth once before the while loop
    # ends
    is_second_pass: bool = False
    # lists of x and y positions
    s_x = [0]
    s_y = [HUMAN_HEIGHT]
    final_height = MAMMOTH_HEIGHT

    while (s_y[-1] >= final_height) or (not is_second_pass):
        # update Fdx and Fdy on each iteration
        Fdx = 0.5 * C_d * v_x**2 * rho * Ax
        Fdy = 0.5 * C_d * v_y**2 * rho * Ay + m * g

        v_x -= Fdx/m * dt
        v_y -= Fdy/m * dt
        
        s_x.append(s_x[-1] + v_x * dt)
        s_y.append(s_y[-1] + v_y * dt)

        if s_y[-1] >= MAMMOTH_HEIGHT:
            is_second_pass = True
        
        # it just works
        if (
            (s_x[-1] > DISTANCE_FROM_HUMAN + MAMMOTH_WIDTH and s_y[-1] > MAMMOTH_HEIGHT)
            or (s_x[-1] < DISTANCE_FROM_HUMAN and s_y[-1] < MAMMOTH_HEIGHT)
        ) and (s_x[-1] > DISTANCE_FROM_HUMAN / 2):
            final_height = 0
        elif (s_x[-1] >= DISTANCE_FROM_HUMAN) and ((s_y[-1] < MAMMOTH_HEIGHT) and s_y[-1] > 0 
            and s_x[-1] < DISTANCE_FROM_HUMAN + MAMMOTH_WIDTH):
            break

    return s_x, s_y


if __name__ == "__main__":
    s_x, s_y = spear_trajectory(vi)
    plt.plot(s_x, s_y)
    plt.xlim(0)
    plt.xlabel('Horizontal position')
    plt.ylim(0)
    plt.ylabel('Vertical position')
    plt.title("Position of spear after being thrown at Mammoth")
    plt.axhline(MAMMOTH_HEIGHT, color='r')
    plt.show()