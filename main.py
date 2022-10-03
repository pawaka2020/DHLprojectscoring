import pandas as _pandas
import functions as func
import classes as cl
import score_prospect as sp
import score_suspect as ss
import score_lead as sl

#TODO: make sure weights can be determined here before plugging in to the score functions.
df = _pandas.read_csv('data.csv')
func.cleanup_names(df)
func.merge_names(df)
ss.score(df, cl.Weights)
sp.score(df, cl.Weights)
sl.score(df, cl.Weights)
print(df[['Customer Name','Suspect Score', 'Prospect Score', 'Lead Score']])