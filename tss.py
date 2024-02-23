## First Line

# Import pandas library
import pandas as pd

# Load dataset
data = pd.read_csv('../dat/C00368/data.csv')

# Print headers of columns
print("Column Headers:", data.columns)

# Test: Print 5 columns
print("First five rows:")
print(data.head())
