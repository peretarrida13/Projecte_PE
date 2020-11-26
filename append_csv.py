import os
import pandas as pd

direct_files = os.listdir()
csv_file = []
for file in direct_files:
    if file.endswith(".csv"):
        csv_file.append(file)

combined_csv = pd.concat([pd.read_csv(f) for f in csv_file])
combined_csv.to_csv( "prova.csv", index=False, encoding='utf-8-sig')