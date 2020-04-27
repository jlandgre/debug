import pandas as pd
import numpy as np
import datetime as dt

#Debug library functions
def init():
    data = {'Desc':[], 'colname':[], 'size':[], 'dtype_string':[], 'dtype_int':[],
            'dtype_float':[], 'isnull':[], 'notnull':[], 'Desc2':[], 'Val2':[], 'time':[]}
    dfDebug = pd.DataFrame(data=data)

    #Trick Pandas into dtyping count columns as integer
    dfDebug.loc[0,:] = ['Dummy_val','',0,0,0,0,0,0,'','',0]
    lst_count_cols = ['size','dtype_string', 'dtype_int', 'dtype_float', 'isnull', 'notnull']
    dfDebug[lst_count_cols] = dfDebug[lst_count_cols].astype('int')

    return dfDebug

def CountDTypeString(df, col):
    return df.loc[df[col].apply(lambda x: isinstance(x, str)), col].size
def CountDTypeInt(df, col):
    return int(df.loc[df[col].apply(lambda x: isinstance(x, int)), col].size)
def CountDTypeFloat(df, col):
    return int(df.loc[df[col].apply(lambda x: isinstance(x, float)), col].size)
def CountNull(df, col):
    return int(df.loc[df[col].isnull(), col].size)
def CountNotNull(df, col):
    return int(df.loc[~df[col].isnull(), col].size)

#Add a new row to dfDebug
def loginfo(dfDebug, logtype, desc, df=None, col='', desc2='', val2=''):

    #Construct row as a list of values and append row to dfDebug
    if logtype == 'colinfo':
        lst = [desc, col, df[col].size, CountDTypeString(df, col), CountDTypeInt(df, col),
               CountDTypeFloat(df, col), CountNull(df, col), CountNotNull(df, col), desc2, val2, '']
    elif logtype == 'indexsize':
        lst = [desc,'',df.index.size, '', '', '', '', '', desc2, val2, '']
    elif logtype == 'time':
        lst = [desc, '', '', '', '', '', '', '', desc2, val2, dt.datetime.now().strftime('%H:%M:%S.%f')]
    elif logtype == 'info':
        lst = [desc, '','', '','', '','', '', desc2, val2, '']
    dfDebug.loc[dfDebug.index.size] = lst

    #Control dtype of count columns for nicer display
    if dfDebug.loc[0,'Desc'] == 'Dummy_val':
        dfDebug.drop(0, axis=0, inplace=True)
        dfDebug.reset_index(drop=True, inplace=True)
    lst_count_cols = ['size','dtype_string', 'dtype_int', 'dtype_float', 'isnull', 'notnull']
    dfDebug[lst_count_cols] = dfDebug[lst_count_cols].astype('str')
    return dfDebug
