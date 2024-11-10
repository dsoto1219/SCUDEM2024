from trajectory import spear_trajectory
from constants import rock_density, MAMMOTH_HEIGHT, TO_PSI
from lethality import lethality
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from SALib.sample import saltelli
from SALib.analyze import sobol
from scipy.constants import pi


np.seterr(all='raise')

### THROWN PROBLEM ###
throw_problem = {
    'num_vars' : 5,
    'names' : ['a', 'b', 'c',
               'theta',
               'vi'],
    'bounds' : [[1, 50],
                [1, 50],
                [1, 50],
                [0, 0.5 * pi],
                [15, 30]]
}


M = (5500 + 7300) / 2 
vf = 8.49376
Ekf = 0.5 * M * vf**2

param_values = saltelli.sample(throw_problem, 2048)

thrown_energies = np.zeros(param_values.shape[0])

for i, (a, b, c, theta, vi) in tqdm(enumerate(param_values)):
    vi_vec = (vi * np.cos(theta), vi * np.sin(theta))

    # Spear lethality
    Ax = (2*b) * (2*c)
    Ay = a * c 
    # vol = length * width * height / 3
    volume = (a * (2*b) * (2*c)) / 3
    if volume == 0:
        continue
    A = (Ax, Ay)
    m = rock_density * volume
    s_x, s_y, v_fx, v_fy, f_height = spear_trajectory(vi_vec, A, m, dt=1e-1)
    if f_height == 0:
        thrown_energies[i] = -1
    else:
        thrown_energies[i] = lethality(v_fx, v_fy, a, b, c, m)

print(len(thrown_energies))
if all(x == -1 for x in thrown_energies):
    print("Oh no!")

Si = sobol.analyze(throw_problem, thrown_energies, print_to_console=True)

# Extract the sensitivity indices
parameters = throw_problem['names']
S1 = Si['S1']
ST = Si['ST']

# Set up the plot
fig, axs = plt.subplots(figsize=(6, 2))

# Positions of the bars on the x-axis
indices = np.arange(len(parameters))

# Width of a bar
width = 0.35

# Plotting
bar1 = axs.bar(indices, S1, width, label='First-order')
bar2 = axs.bar(indices + width, ST, width, label='Total-order')

# Labels, title, and legend
axs.set_xticks(indices + width / 2)
axs.set_xticklabels(parameters)
axs.set_ylabel('Sensitivity Index')
axs.set_title('Sobol Sensitivity Indices for Thrown Spear Model')
axs.legend()

plt.show()


# charging_lethalities = []
# biggest = 0
# for a, b, c in tqdm(itertools.product(range(1, N+1, step), repeat=3)):
#     # Metrics are in cm, change to m
#     a /= 100
#     b /= 100
#     c /= 100

#     # Charging lethality
#     F = Ekf/a
#     charging_lethalities.append(((a, b, c), F))