import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('WIKI-PRICES.csv')
df.drop(df.index['25:'], inplace=True)
print(df)
