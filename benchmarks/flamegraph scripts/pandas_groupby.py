#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'modin/benchmarks'))
	print(os.getcwd())
except:
	pass
#%% [markdown]

#%%
import pandas as pd

#%%
df = pd.read_csv("Team_Records.csv")

#%%
teams = df.groupby(['Team']).mean()



