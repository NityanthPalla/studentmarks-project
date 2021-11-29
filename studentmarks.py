import csv
import numpy as np
marks=[]
attendance=[]
with open("studentmarks.csv")as f:
    df=csv.DictReader(f)
    for row in df:
        marks.append(float(row["Marks In Percentage"]))
        attendance.append(float(row["Days Present"]))
correlation=np.corrcoef(marks,attendance)
print("Correlation between size of the tv and the time spent on it",correlation[0,1])
 