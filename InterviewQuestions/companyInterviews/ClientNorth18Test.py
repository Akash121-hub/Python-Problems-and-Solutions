"""import csv
import pandas as pd
import codecs
with codecs.open(r"/Users/akash/samplecsv.csv",'r',encoding="utf-8",errors='ignore') as csv_file:
    # lines = pd.read_csv(csv_file)
    data = csv.reader(csv_file)
    next(data)
    # for i in data:
    #     print(list(i))
    # if lines:
    #     print("y")
    # else:
    #     print("n")
"""
import re
list1 = ["Akash Shinde", "Akshay Shinde","Akshay Bhere"]
results = []
for i in list1:
    x = re.search("^Ak.*Sh", i)
    if x:
        results.append(x)
    else:
        continue

print(results)