# Autor: Ethan Kalika
# Date: August 19, 2023

# This script combines the table created by toCSV with the monthly_variables_total.csv table

# Library Imports
import os
from pathlib import Path
import pandas as pd

# Merges the monthly_variables_total.csv table and the monthlyTable.csv into a table called mainAndMonthlyTable.csv
monthly_variables_totalPath = os.path.join(Path(__file__).parent, 'monthly_variables_total.csv')
monthly_variables_totalDf = pd.read_csv(monthly_variables_totalPath, index_col = 0)
monthlyTablePath = os.path.join(Path(__file__).parent, 'monthlyTable.csv')
monthlyTableDf = pd.read_csv(monthlyTablePath, index_col = 0)
savePath = os.path.join(Path(__file__).parent, 'mainAndMonthlyTable.csv')
monthlyTableDf.set_index(["ID's", "Date"], inplace = True)
monthly_variables_totalDf.set_index(["Alliance ID", "Month ID"], inplace = True)
monthly_variables_totalDf = monthly_variables_totalDf[~monthly_variables_totalDf.index.duplicated(keep='first')]
monthly_variables_totalDf.to_csv(os.path.join(Path(__file__).parent, 'tempMain.csv'))
monthlyTableDf.to_csv(os.path.join(Path(__file__).parent, 'tempMonthly.csv'))
'''
duplicated_indexes = monthly_variables_totalDf.index.duplicated(keep=False)
duplicated_rows = monthly_variables_totalDf[duplicated_indexes]
print(duplicated_rows)
'''
mainandMonthlyTableDf = pd.concat([monthly_variables_totalDf, monthlyTableDf], axis = 1)
mainandMonthlyTableDf.to_csv(savePath)
print("done")