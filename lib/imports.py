def load_nxs(path):
    import numpy as np
    import pandas as pd
    import nexusformat.nexus as nx
    f = nx.nxload(path)
    nbframes = np.array(f['entry']['instrument']['xspress3']['channel00']['histogram'][:]).shape[0]
    eresolution = np.array(f['entry']['instrument']['xspress3']['channel00']['histogram'][:]).shape[1]
    energies = np.linspace(25, 204.775, eresolution)

    df0 = pd.DataFrame(f['entry']['instrument']['xspress3']['channel00']['histogram'][:], columns=energies)
    df1 = pd.DataFrame(f['entry']['instrument']['xspress3']['channel01']['histogram'][:], columns=energies)

    df0c = df0.iloc[:, 150:4094]
    df1c = df1.iloc[:, 150:4094]

    return (df0c, df1c)
