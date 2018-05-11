```python
from aide_design.play import*
import matplotlib.pyplot as plt
import numpy as np
marbles_1 = pd.read_csv('Experiment_1_Marbles.csv')
marbles_2 = pd.read_csv('Experiment_2_Marbles.csv')
marbles_3 = pd.read_csv('Experiment_3_Marbles.csv')
rocks_dry_1 = pd.read_csv('Experiment_1_Rocks_Dry.csv')
rocks_dry_2 = pd.read_csv('Experiment_2_Rocks_Dry.csv')
rocks_dry_3 = pd.read_csv('Experiment_3_Rocks_Dry.csv')
rocks_wet_1 = pd.read_csv('Experiment_1_Rocks_Wet.csv')
rocks_wet_2 = pd.read_csv('Experiment_2_Rocks_Wet.csv')
rocks_wet_3 = pd.read_csv('Experiment_3_Rocks_Wet.csv')
marbles = marbles_1 + marbles_2 + marbles_3
marbles_total = np.sum(marbles)
print(np.sum(marbles_total))
rocks_dry = rocks_dry_1 + rocks_dry_2 + rocks_dry_3
rocks_dry_total = np.sum(rocks_dry)
print(np.sum(rocks_dry_total))
rocks_wet = rocks_wet_1 + rocks_wet_2 + rocks_wet_3
rocks_wet_total = np.sum(rocks_wet)
print(np.sum(rocks_wet_total))

fig, ax = plt.subplots()
im = ax.pcolormesh(marbles)
fig.colorbar(im)
plt.savefig('marbles')
plt.show()

fig, ax = plt.subplots()
im = ax.pcolormesh(rocks_wet)
fig.colorbar(im)
plt.savefig('rocks_wet')
plt.show()

fig, ax = plt.subplots()
im = ax.pcolormesh(rocks_dry)
fig.colorbar(im)
plt.savefig('rocks_dry')
plt.show()




```
