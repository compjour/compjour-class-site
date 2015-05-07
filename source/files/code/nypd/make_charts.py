import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline

alldata = pd.read_csv("excerpted-stop-and-frisks-2003-2014.csv")
mydf = alldata.query('race == "B" | race == "W" | race == "Q"')

g = sns.FacetGrid(mydf, col = 'race')
g.map(plt.hist, "year")



###############

PFCOLS = ["pf_hands","pf_wall","pf_grnd","pf_drwep","pf_ptwep","pf_baton","pf_hcuff","pf_pepsp","pf_other"]
WEAPCOLS = ['pistol', 'riflshot', 'asltweap', 'knifcuti', 'machgun', 'othrweap']

YEARS = alldata['year'][pd.notnull(alldata['year'])].unique().astype('int')
dfb = df[df['race'] == 'B']
dfw = df[df['race'] == 'W']


races = ['B', 'W']
d = {}
for race in races:
    dfx = df[df['race'] == race]
    z = pd.DataFrame(index = YEARS)
    ### count trespasses by year
    q = dfx[dfx['frisked'] == "Y"].groupby('year').count()
    z['frisked_count'] = q.ix[:,0]

    q = dfx[dfx['searched'] == "Y"].groupby('year').count()
    z['searched_count'] = q.ix[:,0]

    q = dfx.query(" | ".join(["%s == 'Y'" % w for w in WEAPCOLS])).groupby('year').count()
    z['weapon_found_count'] = q.ix[:,0]

    q = dfx.query(" | ".join(["%s == 'Y'" % w for w in PFCOLS])).groupby('year').count()
    z['force_used_count'] = q.ix[:,0]

    d[race] = z
