import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from SALib.sample import saltelli
from SALib.analyze import sobol

### CHARGING PROBLEM
charging_problem = {
    'num_vars' : 2,
    'names' : ['Mammoth_mass',
               'vf'],
    'bounds' : [[5500, 7300],
                [5, 10]]
}

# vf = 8.49376

param_values = saltelli.sample(charging_problem, 2 ** 15)

charging_energies = np.zeros(param_values.shape[0])

for i, (M, vf) in tqdm(enumerate(param_values)):
    Ekf = 0.5 * M * vf**2
    charging_energies[i] = Ekf

Si = sobol.analyze(charging_problem, charging_energies, print_to_console=True)

# Extract the sensitivity indices
parameters = charging_problem['names']
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
axs.set_title('Sobol Sensitivity Indices for Charging Mammoth Model')
axs.legend()

plt.savefig("charging_model.png")