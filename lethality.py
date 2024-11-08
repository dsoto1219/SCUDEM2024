from constants import vi, m, threshold, a, b
from trajectory import spear_trajectory


def lethality(vi) -> float:
    """
    Returns 1 if the spear throw will kill the mammoth;
    returns float between 0 and 1 otherwise, giving
    a measure of how close to being lethal the throw is.
    """
    _, _, v_x, v_y = spear_trajectory(vi)

    # Energy transferred to the skin at the moment of impact
    delta_E = (0.5*m*(v_x**2 + v_y**2))
    F = delta_E/(a/100)
    pressure = F/((b/50)**2) # in pascals (N/m^2)

    if pressure > threshold:
        return 1
    return (pressure/threshold)**2


if __name__ == "__main__":
    print(lethality(vi))