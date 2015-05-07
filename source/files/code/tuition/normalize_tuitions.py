# make a row for every year

tuition_rows = []
for row in rows:
    if len(tuition_rows) == 0:
        pass
    else:
        lastyr, lastcost = tuition_rows[-1]
        tuition_rows.extend([[lastyr + i, lastcost] for i in range(1, row[0] - lastyr)])
    tuition_rows.append(row)

tuition_df = pd.DataFrame(tuition_rows, columns = ['year', 'tuition'])
