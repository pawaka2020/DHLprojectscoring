#cleans up names
#usually the names come as automated web crawling names which may have errors 
#(ex zzzzzzFAB INDUSTRIES SDN BHD)
def	cleanup_names(df):
	name = 'Customer Name'
	df[name] = df[name].str.replace('[a-z]', '', regex=True)
	df[name] = df[name].str.replace('[:-@]', '', regex=True)
	df[name] = df[name].str.replace('[!-/]', '', regex=True)
	df[name] = df[name].str.replace(' +', ' ', regex=True)
	df[name] = df[name].str.strip()

#TODO: merge function
#def	merge_names(db):

def	setscore_earning(df, type):
	if type == 0:
		df.loc[df['Earning'] > 24999, ['tmp']] = 5
		df.loc[df['Earning'] < 25000, ['tmp']] = 4
		df.loc[df['Earning'] < 14999, ['tmp']] = 3
		df.loc[df['Earning'] < 9999, ['tmp']] = 2
		df.loc[df['Earning'] < 4999, ['tmp']] = 1
		df.loc[df['Earning'] < 0, ['tmp']] = 0
		df['Rank'] = df['Rank'] + df['tmp']
	elif type == 1:
		df.loc[df['Earning'] > 24999, ['tmp']] = 1.0
		df.loc[df['Earning'] < 25000, ['tmp']] = 0.8
		df.loc[df['Earning'] < 14999, ['tmp']] = 0.6
		df.loc[df['Earning'] < 9999, ['tmp']] = 0.4
		df.loc[df['Earning'] < 4999, ['tmp']] = 0.2
		df.loc[df['Earning'] < 0, ['tmp']] = 0
		df['Rank'] = round(df['Rank'] * df['tmp'], 1)
	del df['tmp']

def	setscore_seasonality(df, type):
	if type == 0:
		df.loc[df['Seasonality'] == 'seasonal', ['tmp']] = 5
		df.loc[df['Seasonality'] == 'non-seasonal', ['tmp']] = 0
		df['Rank'] = df['Rank'] + df['tmp']
	elif type == 1:
		df.loc[df['Seasonality'] == 'seasonal', ['tmp']] = 1.0
		df.loc[df['Seasonality'] == 'non-seasonal', ['tmp']] = 0.8
		df['Rank'] = round(df['Rank'] * df['tmp'], 1)
	del df['tmp']

#def	setscore_volume(df, type):

def	setrank_default(df, type):
	if type == 0:
		df['Rank'] = 0
	else:
		df['Rank'] = 1

def	setscore(df, type):
	setrank_default(df, type)
	setscore_earning(df, type)
	setscore_seasonality(df, type)