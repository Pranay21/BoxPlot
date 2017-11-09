import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("ENB2012_data.xlsx", "Sheet1")  
print(df)
fig,ax1 = plt.subplots(figsize = (12,8))
ax1.set_xlabel('Orientation')

df.boxplot(column = ['X6'], vert = 0);
plt.show()