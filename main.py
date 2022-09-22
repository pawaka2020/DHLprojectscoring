import pandas as _pandas
import scoring as _scoring
import functions as _functions

#source fo dummy file: https://docs.google.com/spreadsheets/d/1pctetYR-1DN2TSixeYP_U0mg-mZSEzc9frdPxIFxjms/edit#gid=1341223234
df = _pandas.read_csv('Copy of Dummy Data.csv')
#cleannames(df)
#cleanphones(df)
#mergenames(df)
_functions.cleanup_names(df)
_scoring.setscore(df)
#sort_by_score(df) 
print(df[['Customer Name', 'SCORE']])