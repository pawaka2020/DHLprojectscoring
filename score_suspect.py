#Denotes whether or not a business is to customers (B2C) or to other businesses (B2B)
#According to discussions with DHL team we decided to give B2C the optimum score
#B2B is slightly lower at 8
def	channel(df, weight):
	data = df['Physical Channel']
	df.loc[data == 'B2C', ['tmp']] = 10
	df.loc[data == 'B2B', ['tmp']] = 8
	df.loc[data.isnull(), ['tmp']] = 0
	df['Suspect Score'] = df['Suspect Score'] + (df['tmp'] * weight)

#This is the sum of Facebook followers
#According to https://www.metricmarketing.com/faqs/often-post-social-media/
#A 'good enough' benchmark is around 10000 so we base the optimum score of 10 from that number
def	fbfollowers(df, weight):
	data = df['FB Followers']
	df.loc[data > 9999, ['tmp']] = 10
	df.loc[data < 10000, ['tmp']] = 8
	df.loc[data < 8000, ['tmp']] = 6
	df.loc[data < 6000, ['tmp']] = 6
	df.loc[data < 4000, ['tmp']] = 6
	df.loc[data < 2000, ['tmp']] = 4
	df.loc[data == 0, ['tmp']] = 0
	df.loc[data.isnull(), ['tmp']] = 0
	df['Suspect Score'] = df['Suspect Score'] + (df['tmp'] * weight)

#This is the sum of Instagram followers
#According to https://blog.sellfy.com/how-many-instagram-followers-to-make-money/
#A 'good enough' benchmark is around 1000 so we base the optimum score of 10 from that number
def	igfollowers(df, weight):
	data = df['IG Followers']
	df.loc[data > 999, ['tmp']] = 10
	df.loc[data < 1000, ['tmp']] = 8
	df.loc[data < 800, ['tmp']] = 6
	df.loc[data < 600, ['tmp']] = 6
	df.loc[data < 400, ['tmp']] = 6
	df.loc[data < 200, ['tmp']] = 4
	df.loc[data == 0, ['tmp']] = 0
	df.loc[data.isnull(), ['tmp']] = 0
	df['Suspect Score'] = df['Suspect Score'] + (df['tmp'] * weight)

#whether or not a business as a website or an online store (on Shopee, Lazada, etc)
#it's either yes, no or no info, 10 or 0.
def	website(df, weight):
	data = df['Has Website']
	df.loc[data == 'Yes', ['tmp']] = 10
	df.loc[data == 'No', ['tmp']] = 0
	df.loc[data.isnull(), ['tmp']] = 0
	df['Suspect Score'] = df['Suspect Score'] + (df['tmp'] * weight)

#whether or not a business uses foreign currency
#it's an indication of international shipping = more revenue, more potential need for DHL's services.
#it's either yes, no or no info, 10 or 0.
def	foreigncurrency(df, weight):
	data = df['Uses Foreign Currency']
	df.loc[data == 'Yes', ['tmp']] = 10
	df.loc[data == 'No', ['tmp']] = 0
	df.loc[data.isnull(), ['tmp']] = 0
	df['Suspect Score'] = df['Suspect Score'] + (df['tmp'] * weight)

#whether or not a business is a part of a membership or association(ie Malaysian Wood Industries Association)
#if it's a member, it may be a more serious business with high revenues and volume of goods delivered.
def	membership(df, weight):
	data = df['Has Membership']
	df.loc[data == 'Yes', ['tmp']] = 10
	df.loc[data == 'No', ['tmp']] = 0
	df.loc[data.isnull(), ['tmp']] = 0
	df['Suspect Score'] = df['Suspect Score'] + (df['tmp'] * weight)

def	score(df, Weights):
	df['Suspect Score'] = 0
	channel(df,Weights.ch)
	fbfollowers(df,Weights.fb)
	igfollowers(df,Weights.ig)
	website(df,Weights.web)
	foreigncurrency(df,Weights.fc)
	membership(df,Weights.mem)
	del df['tmp']
	#print(df[['Customer Name','Has Website','SCORE']])