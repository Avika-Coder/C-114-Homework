from google.colab import files
data_to_load=files.upload()

import pandas as pd
import csv
import plotly.express as px
import statistics
df=pd.read_csv("main114.csv")
TOEFL_Score=df["TOEFL Score"].tolist()
Chance_of_Admit=df["Chance of Admit "].tolist()
graph1=px.scatter(x=TOEFL_Score,y=Chance_of_Admit)
graph1.show()

m=1
c=0
y=[]
for x in TOEFL_Score:
  y_value=m*x+c
  y.append(y_value)
graph2=px.scatter(x=TOEFL_Score,y=Chance_of_Admit)
graph2.update_layout(shapes=[dict(type='line',y0=min(y),y1=max(y),x0=min(TOEFL_Score),x1=max(TOEFL_Score))])
graph2.show()

import numpy as np
TOEFL_array=np.array(TOEFL_Score)
Chances_array=np.array(Chance_of_Admit)
m,c=np.polyfit(TOEFL_array,Chances_array,1)
y=[]
for x in TOEFL_array:
  y_value=m*x+c
  y.append(y_value)

graph3=px.scatter(x=TOEFL_array,y=Chances_array)
graph3.update_layout(shapes=[dict(type='line',y0=min(y),y1=max(y),x0=min(TOEFL_array),x1=max(TOEFL_array))])
graph3.show()

x=250
y= m*x+c
print(f"Chances of admit if TOEFL Score {x} is {y}")

x=int(input("Enter your TOEFL Score : "))
y=m*x+c
print(f"Chances of admit if TOEFL Score {x} is {y}")
