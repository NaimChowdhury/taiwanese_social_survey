## First Line

# Import pandas library
import pandas as pd

# Load datasets
dtafile_law_society = '../dat/C00368/data.csv'
dtafile_summary_2020 = '../dat/C00369/tscs2020q1.dta'
dtafile_family_2020 = '../dat/C00390/tscs2021q1.dta'


df_law_society = pd.read_csv(dtafile_law_society)
df_summary_2020 = pd.read_stata(dtafile_summary_2020)
df_family_2020 = pd.read_stata(dtafile_family_2020)


# Print headers of columns of Law and Society
print("Column Headers:", df_law_society.columns)

# Test: Print 5 columns
print("First five rows:")
print(df_law_society.head())

