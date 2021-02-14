import csv 
import pandas as pd 
import plotly.express as px
with open("class2.csv",newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
totalmarks = 0 
totalenteries = len(filedata)
for marks in filedata :
    totalmarks = totalmarks+float(marks[1])
mean = totalmarks/totalenteries
print(mean)
df = pd.read_csv('class2.csv')
fig = px.scatter(df,x = 'StudentNumber',y = 'Marks')
fig.update_layout(shapes = [dict(type = 'line',y0 = mean,y1 = mean,x0 = 0,x1 = totalenteries)])
fig.update_yaxes(rangemode = 'tozero')
fig.show()