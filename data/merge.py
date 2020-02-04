import pandas as pd

mat = pd.read_csv('student-mat.csv', sep = ',')
por = pd.read_csv('student-por.csv', sep = ',')

totale =pd.merge(mat, por, on = ["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"])
print(totale.head())