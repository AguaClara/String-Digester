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
rocks_dry = rocks_dry_1 + rocks_dry_2 + rocks_dry_3
rocks_wet = rocks_wet_1 + rocks_wet_2 + rocks_wet_3
plt.imshow(marbles, cmap='hot', interpolation='nearest')
plt.savefig('marbles')
plt.show()
plt.imshow(rocks_wet, cmap='hot', interpolation='nearest')
plt.savefig('rocks_wet')
plt.show()
plt.imshow(rocks_dry, cmap='hot', interpolation='nearest')
plt.savefig('rocks_dry')
plt.show()


```
