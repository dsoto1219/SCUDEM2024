import matplotlib.pyplot as plt
import numpy as np
from horizontal_cross_section import cayley_menger_area_3points
from vertical_cross_area import cayley_menger_area_4points
from constants import C_d, rho, m, g, a, b, c, DISTANCE_FROM_HUMAN, MAMMOTH_HEIGHT, MAMMOTH_WIDTH, HUMAN_HEIGHT, vi


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
    v_fx = v_x
    v_fy = v_y
    return s_x, s_y, v_fx, v_fy


if __name__ == "__main__":
    s_x, s_y, _, _ = spear_trajectory(vi)
    plt.plot(s_x, s_y)
    plt.xlim(0)
    plt.xlabel('Horizontal position')
    plt.ylim(0)
    plt.ylabel('Vertical position')
    plt.title("Position of spear after being thrown at Mammoth")
    plt.axhline(MAMMOTH_HEIGHT, color='r')
    plt.show()