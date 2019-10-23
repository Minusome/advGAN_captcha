# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Data
df=pd.DataFrame(
    {
        'epoch': range(1,22),
        'weighted-normal': [4.371316306, 85.75638507, 36.2475442, 78.58546169, 84.13555992, 96.80746562, 60.31434185, 51.66994106, 45.23575639, 26.22789784, 86.64047151, 55.35363458, 39.04715128, 83.93909627, 47.8388998, 56.72888016, 43.86051081, 41.35559921, 49.45972495, 12.62278978, 65.32416503],
        'weighted-adv': [10.65815324, 90.86444008, 68.32023576, 84.03732809, 54.12573674, 96.26719057, 82.66208251, 90.5697446, 51.27701375, 55.35363458, 94.79371316, 80.74656189, 68.95874263, 94.10609037, 83.74263261, 88.4086444, 78.92927308, 59.67583497, 67.14145383, 17.23968566, 92.82907662], 
        'unweighted-normal': [51.2278978, 66.8467583, 80.697446, 66.9449902, 53.0451866, 85.21611, 93.762279, 97.3477407, 83.4479371, 75.9332024, 65.2750491, 60.7072692, 79.9115914, 97.3477407, 58.7917485, 59.7249509, 80.8939096, 88.8998035, 55.6483301, 97.2003929, 60.3143418],
        'unweighted-adv': [65.2750491, 81.4341847, 93.8605108, 96.4145383, 90.8644401, 98.0353635, 96.611002, 94.9410609, 97.740668, 96.3163065, 92.4361493, 91.7976424, 95.1866405, 98.3791749, 88.5559921, 82.2691552, 91.9449902, 95.6777996, 83.5952849, 98.280943, 84.4302554]
    }
)
 
plt.title('Unweighted Adversarially Trained Solver Accuracy Per Epoch')
plt.plot( 'epoch', 'unweighted-normal', data=df, marker='', linewidth=2, label='Normal')
plt.plot( 'epoch', 'unweighted-adv', data=df, marker='', linewidth=2, label='Adversarial')

plt.xlabel('Epoch Number')
plt.xticks(range(1,22))
plt.ylabel('Accuracy (%%)')
plt.legend()

plt.show()

plt.clf()

plt.title('Weighted Adversarially Trained Solver Accuracy Per Epoch')
plt.plot( 'epoch', 'weighted-normal', data=df, marker='', linewidth=2, label='Normal')
plt.plot( 'epoch', 'weighted-adv', data=df, marker='', linewidth=2, label='Adversarial')

plt.xlabel('Epoch Number')
plt.xticks(range(1,22))
plt.ylabel('Accuracy (%%)')
plt.legend()

plt.show()