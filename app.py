import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ds_salaries.csv')

df['company_size'].value_counts().plot(kind='bar')

plt.tight_layout()
plt.savefig('/mnt/c/Users/chelseam/OneDrive - Full Sail University/Desktop/Data Visualization and Modeling/Repo_Template/company_size.png')  # Save to a Windows-accessible location
plt.close()
