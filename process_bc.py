import pandas as pd
import numpy as np


def process_bank_df(df):
    df.index = range(df.shape[0])
    df=df.drop(df.index[df.loc[:,'BareNuclei'] =='?'])
    df.index = range(df.shape[0])
    df = df[['Benign', 'ClumpThickness', 'UniformityOfCellSize',
               'UniformityOfCellShape', 'MarginalAdhesion', 'SingleEpithelialCellSize',
               'BareNuclei', 'BlandChromatin', 'NormalNucleoli', 'Mitoses']].astype(int)
    df['Benign'] = (df['Benign'] - 2)//2
    return df

if __name__ == '__main__':
    df = pd.read_csv('data/breast-cancer-wisconsin.data', names=['ClumpThickness', 'UniformityOfCellSize',
               'UniformityOfCellShape', 'MarginalAdhesion', 'SingleEpithelialCellSize',
               'BareNuclei', 'BlandChromatin', 'NormalNucleoli', 'Mitoses', 'Benign'])
    df = process_bank_df(df)
    df.to_csv('data/breastcancer_data.csv', index=False)