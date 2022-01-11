def minmax(x):
    import numpy as np
    return np.min(x)-1,np.max(x)+1

def extract_between(lst,start,end):
    import numpy as np
    #print(lst)
    for i in lst:

        if i < end and i >= start :

            return i
    return np.nan

def extract_ss_mean(df):
    import numpy as np
    return (np.mean(df.iloc[:,1][15:30]))