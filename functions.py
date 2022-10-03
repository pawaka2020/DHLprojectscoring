#cleans up names
#usually the names come as automated web crawling names which may have errors 
#(ex zzzzzzFAB INDUSTRIES SDN BHD)

#TODO: merge function
#def	merge_names(db):
def	cleanup_names(df):
	name = 'Customer Name'
	df[name] = df[name].str.replace('[a-z]', '', regex=True)
	df[name] = df[name].str.replace('[:-@]', '', regex=True)
	df[name] = df[name].str.replace('[!-/]', '', regex=True)
	df[name] = df[name].str.replace(' +', ' ', regex=True)
	df[name] = df[name].str.strip()


	#df[data] = df[data] + 0
	#print(df[['Customer Name','Total Potential Revenue/Month']])