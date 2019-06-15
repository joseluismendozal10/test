import os
import csv

csvpath= os.path.join("cereal.csv")
with open(csvpath, newline='') as cvsfile:
    cerealDF= csv.reader(cvsfile, delimiter= ',')
    next(cerealDF,None)
    
    for i in cerealDF:
        if float (i[7])>= float(5):
            print(i)
        
        
        
