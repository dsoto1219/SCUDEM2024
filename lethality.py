from constants import TO_PSI


def lethality(v_fx, v_fy, a, b, c, mass) -> float:
    """
    Returns 1 if the spear throw will kill the mammoth;
    returns float between 0 and 1 otherwise, giving
    a measure of how close to being lethal the throw is.
    """
    # Energy transferred to the skin at the moment of impact
    delta_E = 0.5 * mass * (v_fx**2 + v_fy**2)
    F = delta_E/a
    pressure = F/((2*b) * (2*c)) # in pascals (N/m^2)

    # return pressure * TO_PSI
    return F
    # if pressure > threshold:
    #     return 1
    # return (pressure/threshold)**2


if __name__ == "__main__":
    print(f"{lethality(vi[0], vi[1], 1, 1, 22)} psi")