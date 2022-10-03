def	weightpackage(df, weight, score):
	data = 'Avg Weight Per Package (kg)'
	df.loc[df[data] == '> 30', ['tmp']] = 10
	df.loc[df[data] == '25 - 30', ['tmp']] = 10
	df.loc[df[data] == '20 - 25', ['tmp']] = 8
	df.loc[df[data] == '15 - 20', ['tmp']] = 6
	df.loc[df[data] == '10 - 15', ['tmp']] = 4
	df.loc[df[data] == '5 - 10', ['tmp']] = 2
	df.loc[df[data] == '0 - 5', ['tmp']] = 0
	df.loc[df[data].isnull(), ['tmp']] = 0
	df[score] = df[score] + (df['tmp'] * weight)

def	broughtinsurance(df, weight, score):
	data = 'Brought Packaging Insurance'
	df.loc[df[data] == 'No', ['tmp']] = 10
	df.loc[df[data] == 'Yes', ['tmp']] = 0
	df.loc[df[data].isnull(), ['tmp']] = 0
	df[score] = df[score] + (df['tmp'] * weight)

def	ctos(df, weight, score):
	data = 'CTOS Score'
	df.loc[df[data] == '744 - 850', ['tmp']] = 10
	df.loc[df[data] == '718 - 743', ['tmp']] = 8
	df.loc[df[data] == '697 - 717', ['tmp']] = 6
	df.loc[df[data] == '651 - 696', ['tmp']] = 4
	df.loc[df[data] == '529 - 650', ['tmp']] = 2
	df.loc[df[data] == '300 - 528', ['tmp']] = 0
	df.loc[df[data].isnull(), ['tmp']] = 0
	df[score] = df[score] + (df['tmp'] * weight)

def	score(df, Weights):
	score = 'Lead Score'
	df[score] = 0
	weightpackage(df,Weights.we, score)
	broughtinsurance(df,Weights.ins, score)
	ctos(df,Weights.ctos, score)
	del df['tmp']
	#print(df[['Customer Name','Has Website','SCORE']])