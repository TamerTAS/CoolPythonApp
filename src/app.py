import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Hello from virtual environment!")

a = np.array([1, 2, 3])
print("Numpy array:", a)

df = pd.DataFrame({"Numbers": [1, 2, 3]})
print(df)

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Plot")
plt.show()
