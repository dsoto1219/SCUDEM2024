import matplotlib.pyplot as plt
import numpy as np

"""Constants that will never change"""
C_d = 0.5 # Drag coefficient/constant, unitless
# velocities, (x, y) pairs resp. (m/s)
rho = 1.225 # air density (kg/m^3)
g = 9.80665 # gravitational constant (m/s^2)

"""Constants that may change, i.e. as initial conditions"""
A = 0.01 # Surface area of the spear (m^2)
m = 0.5 # mass of the spear (kg)
# Heights in m
HUMAN_HEIGHT = 1.8
MAMMOTH_HEIGHT = 3.5
MAMMOTH_WIDTH = MAMMOTH_HEIGHT * 1.25
DISTANCE_FROM_HUMAN = 20
THETA: float = np.radians(45) # angle of the thrown spear
len_of_spear: float = 0.1
area_of_spear_from_front: float = 0.001
threshold: float = 1

vi: tuple = (15*np.cos(THETA), 15*np.sin(THETA))

def area(angle: float) -> float:
    pass
    #return [AREA_X, AREA_Y]

def trajectory(vi: tuple, dt=0.01) -> None:
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
    #t_final = 0

    while (s_y[-1] >= MAMMOTH_HEIGHT) or (not is_second_pass):
        # update Fdx and Fdy on each iteration
        Fdx = 0.5 * C_d * v[-1][0]**2 * rho * A
        Fdy = 0.5 * C_d * v[-1][1]**2 * rho * A + m * g

        v.append(
            (v[-1][0] - Fdx/m * dt, 
             v[-1][1] - Fdy/m * dt))
        
        s_x.append(s_x[-1] + v[-1][0] * dt)
        s_y.append(s_y[-1] + v[-1][1] * dt)

        if s_y[-1] >= MAMMOTH_HEIGHT:
            is_second_pass = True
        
        #t_final+=dt

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