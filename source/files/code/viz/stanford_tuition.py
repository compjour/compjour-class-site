
########################
# Set up inflation calculator

import csv
import requests
url = 'https://raw.githubusercontent.com/datasets/cpi-us/master/data/cpiai.csv'
cpidata = list(csv.reader(requests.get(url).text.splitlines()))
cpidf = pd.DataFrame(cpidata[1:], columns = cpidata[0])
cpidf = pd.DataFrame.convert_objects(cpidf, convert_dates = 'coerce', convert_numeric = True)
cpimean_df = cpidf.groupby(cpidf['Date'].map(lambda x: x.year)).mean()

def adjust_for_inflation(amt, from_year, to_year):
    cpimean_df['Index'][to_year] / cpimean_df['Index'][from_year]
    return round(ratio * amt, 2)



### Now let's graph things
import matplotlib.pyplot as pyplot

# Without inflation
pyplot.plot(tuition_df['year'], tuition_df['tuition'])

# Adjusted for 2014 dollars
tuition_df['adjusted_tuition'] = tuition_df.apply(lambda x: adjust_for_inflation(x['tuition'], x['year'], 2014), axis=1)


# Make a line graph
pyplot.plot(tuition_df['year'], tuition_df['tuition'])
pyplot.plot(tuition_df['year'], tuition_df['adjusted_tuition'])

# Make a bar chart
pyplot.bar(tuition_df['year'], tuition_df['tuition'])
pyplot.bar(tuition_df['year'], tuition_df['adjusted_tuition'])



########### change

tuition_df['tuition_pct_yoy'] = tuition_df.pct_change()['tuition'] * 100
tuition_df['adjusted_tuition_pct_yoy'] = tuition_df.pct_change()['adjusted_tuition'] * 100
cpisum_df = cpidf.groupby(cpidf['Date'].map(lambda x: x.year)).sum()

pyplot.bar(tuition_df['year'], tuition_df['adjusted_tuition_pct_yoy'])
pyplot.bar(cpisum_df.index, cpisum_df['Inflation'])
