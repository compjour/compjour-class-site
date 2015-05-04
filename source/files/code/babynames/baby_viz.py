import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyplot
import csv

%pylab
statedata = pd.read_csv('/tmp/combined-state.csv')




ca_daniels = statedata.query('sex == "M" & name == "Daniel" & state == "CA"')
bar_plot = sns.barplot(x = ca_daniels["year"], y = ca_daniels["count"],
                        palette="muted")
pyplot.xticks(rotation=90)
pyplot.show()
