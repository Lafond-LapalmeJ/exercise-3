import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

populations = ["eas", "afr", "amr", "asj", "sas", "nfe","fin"]

dpyd = pd.read_csv("~/workshop/git/projects/exercise-3/data/dpyd_gnomad.tsv", sep='\t')

var_id = input("Enter a variant ID that you want to plot the allele frequency per population: ")

dpyd['variant_id'] = dpyd['CHROM'].map(str) + "-" + dpyd['START'].map(str) + "-" + dpyd['REF'] + "-" + dpyd['ALT']

var_dpyd = dpyd.loc[dpyd['variant_id'] == var_id]

freq_var = {}

for population in populations:
    ac_pop = 'AC_' + population
    an_pop = 'AN_' + population
    notnull_index = var_dpyd[an_pop].map(str) != 'None'
    freq_var[population] = sum( var_dpyd[ac_pop][notnull_index].map(int) / var_dpyd[an_pop][notnull_index].map(int))

dict = {
    'populations': populations,
    'freq_var': list(freq_var.values())
}

freq_df = pd.DataFrame.from_dict(dict)

sns.set_style("darkgrid")
sns.barplot(x='populations',y = 'freq_var', data=freq_df, color = "skyblue").set_title(var_id)
plt.show()
