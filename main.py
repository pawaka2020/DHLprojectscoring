import pandas as _pandas
import functions as func
#import scoring as _scoring

df = _pandas.read_csv('dhlfile.csv')
#0 for addictive, 1 for multiplicative
func.setscore(df, 1)
print(df.values)