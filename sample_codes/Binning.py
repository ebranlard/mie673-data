import numpy as np
import pandas as pd

# --------------------------------------------------------------------------------}
# --- Binning 
# --------------------------------------------------------------------------------{
def bin_DF(df, xbins, colBin, stats='mean'):
    """ 
    Perform bin averaging of a dataframe
    INPUTS:
      - df   : pandas dataframe
      - xBins: end points delimiting the bins, array of ascending x values
      - colBin: column name (string) of the dataframe, used for binning 
    OUTPUTS:
       binned dataframe, with additional columns 'Counts' for the number 

    """
    if colBin not in df.columns.values:
        raise Exception('The column `{}` does not appear to be in the dataframe'.format(colBin))
    xmid      = (xbins[:-1]+xbins[1:])/2
    df['Bin'] = pd.cut(df[colBin], bins=xbins, labels=xmid ) # Adding a column that has bin attribute
    if stats=='mean':
        df2       = df.groupby('Bin', observed=False).mean()                     # Average by bin
    elif stats=='std':
        df2       = df.groupby('Bin', observed=False).std()                     # std by bin
    # also counting
    df['Counts'] = 1
    dfCount=df[['Counts','Bin']].groupby('Bin', observed=False).sum()
    df2['Counts'] = dfCount['Counts']
    # Just in case some bins are missing (will be nan)
    df2       = df2.reindex(xmid)
    return df2
