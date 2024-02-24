## First Line

# Import pandas library
import pandas as pd

# Load datasets
#dtafile_law_society = '../dat/C00368/data.csv'
#dtafile_summary_2020 = '../dat/C00369/tscs2020q1.dta'
#dtafile_family_2020 = '../dat/C00390/tscs2021q1.dta'
dtafile_national_2013 = '../dat/0604Q2/tscs2013q2.dta'
dtafile_2003 = '../dat/C00111_2/tscs2003q2.dta'

#df_law_society = pd.read_csv(dtafile_law_society)
#df_summary_2020 = pd.read_stata(dtafile_summary_2020)
#df_family_2020 = pd.read_stata(dtafile_family_2020)
df_national_2013 = pd.read_stata(dtafile_national_2013)


# Testing converting the encoding for a single column
#df_national_2013['zip'] = df_national_2013['zip'].apply(lambda x: x.encode('latin-1').decode('big5-tw'))

# Decode to traditional for a single string s.
def decode_traditional(s):
	try:
		return s.encode('latin-1', errors='ignore').decode('big5-tw')
	except AttributeError:
		return s

# Apply the decoding to each string in columns with strings
for col in df_national_2013.columns:
	if df_national_2013[col].dtype == ('category' or 'object'):
		df_national_2013[col] = df_national_2013[col].apply(lambda x: decode_traditional(x))