import pandas as pd
sample_data = pd.read_csv("customers-100.csv")#if no headers then use header=None
print(sample_data.head())
