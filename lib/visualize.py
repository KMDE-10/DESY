def disp_peak_move(df):
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(20,10))
    #display(df)
    for i in df.index:
        for e in df.loc[i,'peak_energies[keV]']:
            ax.scatter(i,e,color='k',s=1)

    plt.show()