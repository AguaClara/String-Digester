```python
from aide_design.play import*
import matplotlib.pyplot as plt
import numpy as np
marbles_1 = pd.read_csv('Experiment_1_Marbles.csv')
marbles_2 = pd.read_csv('Experiment_2_Marbles.csv')
plt.imshow(marbles_1, cmap='hot', interpolation='nearest')
plt.imshow(marbles_2, cmap='hot', interpolation='nearest')


```
