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
print("Correlation between the marks scored and the days present in school is",correlation[0,1])
 
