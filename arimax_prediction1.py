# Using pandas library to generate arimax predition model
# based on sentiment score created from Web Article Data analysis

import numpy as np
import pandas as pd
import pyflux as pf
from datetime import datetime
import matplotlib.pyplot as plt

data = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/MASS/drivers.csv")
data.index = data['time']

f = open( "hpi.txt", "r" )
lines = f.read().split('\n')
hpi = [float(item) for item in lines]
f.close()

f = open( "senti1.txt", "r" )
lines = f.read().split('\n')
senti = [float(item) for item in lines]
f.close()

date = []
month = [ '01','02','03','04','05','06','07','08','09','10','11','12' ]
year = [ '2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017' ]
for i in year:
	for j in month:
		date.append(i + '-' + j + '-01')

#make a dataFrame
data = {'date': date[0:116], 'Web_Article': hpi[0:116], 'senti': senti[0:116]}
df = pd.DataFrame(data, columns = ['date', 'Web_Article', 'senti'])
df['date'] = pd.to_datetime(df['date'])
df.index = df['date']
del df['date']

plt.figure()
plt.plot(df.index, df['Web_Article'])
plt.ylabel('Web_Article')
plt.title('2007-01 ~ 2016-08')

print(df)

model = pf.ARIMAX(data=df, formula='Web_Article~1+senti',ar=1, ma=1, family=pf.Normal())
x = model.fit("MLE")
x.summary()
model.plot_fit()

model.plot_predict(h=12,oos_data=df.iloc[-12:],past_values=100)
temp = model.predict(h=12,oos_data=df.iloc[-12:])
print (type(temp))
print (temp)
plt.show()

