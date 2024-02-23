## First Line

# Import pandas library
import pandas as pd

# Load datasets
#	dtafile_law_society = '../dat/C00368/data.csv'
#	dtafile_summary_2020 = '../dat/C00369/tscs2020q1.dta'
#	dtafile_family_2020 = '../dat/C00390/tscs2021q1.dta'
	dtafile_national_2013 = '../dat/0604Q2/tscs2013q2.dta'
	dtafile_2003 = '../dat/C00111_2/tscs2003q2.dta'


#	df_law_society = pd.read_csv(dtafile_law_society)
#	df_summary_2020 = pd.read_stata(dtafile_summary_2020)
#	df_family_2020 = pd.read_stata(dtafile_family_2020)
	df_national_2013 = pd.read_stata(dtafile_national_2013)
	df_2003 = pd.read_stata(dtafile_2003)

# Data exploration

# Print headers of columns
	# print("Column Headers:", df_law_society.columns)


# Test: Print 5 columns 
#	print("First five rows:")
#	print(df_law_society.head())
#	print(df_summary_2020.head())
#	print(df_family_2020.head())

