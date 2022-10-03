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

#merges duplicate names
#the newer names will take precedent when merging
#then arrange names by unique lead assignment number
def	merge_names(df):
	name = 'Customer Name'
	num = 'Unique Lead Assignment Number'
	df = df.groupby(name).last().reset_index()
	df = df.groupby(num).last().reset_index()