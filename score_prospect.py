#The higher the designation, the higher the score.
def	designation(df, weight, score):
	data = 'Contact person Designation'
	df.loc[df[data] == 'Director & above', ['tmp']] = 10
	df.loc[df[data] == 'Mid-level manager', ['tmp']] = 8
	df.loc[df[data] == 'Senior', ['tmp']] = 6
	df.loc[df[data] == 'Entry level', ['tmp']] = 4
	df.loc[df[data].isnull(), ['tmp']] = 0
	df[score] = df[score] + (df['tmp'] * weight)
	#print(df[[data, score]])

#Fedex higher score because it's similar to DHL in offering higher rate but higher quality services, thus easy to convert.
#Other couriers lower score because they occupy the 'lower cost' niche thus more difficult
#for DHL to convert.
#'Others' even lower score because this implies the company uses an obscure service that possibly have even lower costs or specific niche role, even harder to convert to DHL.
def	competitors(df, weight, score):
	data = 'Competitors'
	df.loc[df[data] != 'FedEx', ['tmp']] = 6
	df.loc[df[data] == 'FedEx', ['tmp']] = 10
	df.loc[df[data] == 'Others', ['tmp']] = 4
	df.loc[df[data].isnull(), ['tmp']] = 0
	df[score] = df[score] + (df['tmp'] * weight)
	#print(df[[data, score]])
	
def	cleanrevenue(df):
	data = 'Total Potential Revenue/Month'
	df[data] = df[data].str.replace('[A-Z]', '', regex=True)
	df[data] = df[data].str.replace(' ', '', regex=True)
	df[data] = df[data].str.replace(',', '', regex=True)
	df.loc[df[data].isnull()] = 0
	df[data] = df[data].astype(int)
	
def	revenue(df, weight, score):
	data = 'Total Potential Revenue/Month'
	cleanrevenue(df)
	df.loc[df[data] > 24999, ['tmp']] = 10
	df.loc[df[data] < 25000, ['tmp']] = 8
	df.loc[df[data] < 14999, ['tmp']] = 6
	df.loc[df[data] < 9999, ['tmp']] = 4
	df.loc[df[data] < 4999, ['tmp']] = 2
	df.loc[df[data] == 0, ['tmp']] = 0
	df[score] = df[score] + (df['tmp'] * weight)
	#print(df[[data, score]])
	
def	score(df, Weights):
	score = 'Prospect Score'
	df[score] = 0
	designation(df, Weights.des, score)
	competitors(df, Weights.comp, score)
	revenue(df, Weights.rev, score)
	del df['tmp']
	