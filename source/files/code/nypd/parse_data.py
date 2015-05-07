from glob import glob
import pandas as pd
WEAPCOLS = ['pistol', 'riflshot', 'asltweap', 'knifcuti', 'machgun', 'othrweap']
PFCOLS = ["pf_hands","pf_wall","pf_grnd","pf_drwep","pf_ptwep","pf_baton","pf_hcuff","pf_pepsp","pf_other"]
STOPCOLS = ["cs_objcs","cs_descr","cs_casng","cs_lkout","cs_cloth","cs_drgtr","cs_furtv","cs_vcrim","cs_bulge","cs_other"]
GENCOLS = ['year', 'pct', 'datestop', 'timestop', 'recstat',
'inout', 'crimsusp', 'arstmade', 'arstoffn', 'sumissue', 'sumoffen', 'frisked', 'searched', 'contrabn', 'xcoord', 'ycoord', 'city']
DEMOCOLS = ['race', 'sex', 'age']
ALL_COLS = WEAPCOLS + PFCOLS + STOPCOLS + GENCOLS + DEMOCOLS

alldf = pd.DataFrame(columns = ALL_COLS)
for csvname in glob('/data-hold/*.csv'):
    print("Adding", csvname)
    df = pd.read_csv(csvname, encoding = ' iso-8859-1')
    alldf = alldf.append(df[ALL_COLS])

# save the file
alldf.to_csv("/data-hold/excerpted-stop-and-frisks-2003-2014.csv")



## Let's do some counting

alldf['year'].value_counts(sort = False)

# 2003    160851
# 2004    313523
# 2005    398191
# 2006    506491
# 2007    472096
# 2008    540302
# 2009    581168
# 2010    601285
# 2011    685724
# 2012    532911
# 2013    191851
# 2014     45787
