import pandas as _pandas
import functions as func
import score_prospect as sp
import score_suspect as ss

#TODO: make sure weights can be determined here before plugging in to the score functions.
df = _pandas.read_csv('data.csv')
func.cleanup_names(df)
ss.score(df)
sp.score(df)
#print(df[['Customer Name','Suspect Score']])