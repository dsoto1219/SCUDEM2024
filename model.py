from trajectory import spear_trajectory
import itertools
from horizontal_cross_section import cayley_menger_area_3points
from vertical_cross_area import cayley_menger_area_4points
from cayley_menger_volume import cayley_menger_volume
from constants import vi, rock_density
from lethality import lethality
import numpy as np
import decimal
from tqdm import tqdm

np.seterr(all='raise')

step = 5
N = 50
lethalities = [] #0] * (N/step)**3
for a, b, c in tqdm(itertools.product(range(1, N+1, step), repeat=3)):
    # Horizontal and vertical Cross-section areas (cm)
    # Dividing by 10000 since each area is in cm^2 but we want m^2
    Ax = (2*b) * (2*c)
    Ay = a * c
    # vol = length * width * height / 3
    volume = (a * (2*b) * (2*c)) / 3
    if 0 in {volume, Ax, Ay}:
        continue
    A = (Ax, Ay)
    print(*A)
    m = rock_density * volume
    try:
        _, _, v_fx, v_fy = spear_trajectory(vi, A, volume, dt=0.01)
    except FloatingPointError:
        print(a, b, c, m, volume)
        break
    lethalities.append(lethality(v_fx, v_fy, m))
    print(volume, m)
    break


print(lethalities)
