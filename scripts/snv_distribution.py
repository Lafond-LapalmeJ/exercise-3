import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

populations = ["eas", "afr", "amr", "asj", "sas", "nfe","fin"]

dpyd = pd.read_csv("~/workshop/git/projects/exercise-3/data/dpyd_gnomad.tsv", sep='\t')

# Only SNV
dpyd = dpyd[dpyd.VARIANT_CLASS == 'SNV']
sns.countplot(x = 'REF', hue= 'ALT', data = dpyd)
plt.show()
