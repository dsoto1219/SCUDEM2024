from constants import vi, threshold, a, b, c, TO_PSI, DISTANCE_FROM_HUMAN
from trajectory import spear_trajectory


def lethality(v_fx, v_fy, mass) -> float:
    """
    Returns 1 if the spear throw will kill the mammoth;
    returns float between 0 and 1 otherwise, giving
    a measure of how close to being lethal the throw is.
    """

    # Energy transferred to the skin at the moment of impact
    delta_E = 0.5 * mass * (v_fx**2 + v_fy**2)
    print(delta_E)
    F = delta_E/DISTANCE_FROM_HUMAN
    pressure = F/((2*b/100) * (2*c/100)) # in pascals (N/m^2)

    return pressure * TO_PSI
    # if pressure > threshold:
    #     return 1
    # return (pressure/threshold)**2


if __name__ == "__main__":
    print(f"{lethality(vi):.1f} psi")