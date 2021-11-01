import pandas as pd
import numpy as np

df = pd.read_csv(r'D:/weather2.csv')
df.columns = ['date','hightest','minimum']
print(df)
weather = pd.isnull(df)
print(np.any(weather))
data = df.dropna()
print(np.all(pd.notna(data)))