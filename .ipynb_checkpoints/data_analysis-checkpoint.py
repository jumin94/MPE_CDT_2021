import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt


path = '/home/julia/Dropbox/Cursos_Materias/MPE_forecast_verification/MPECDT-ForecastVerification/Project4/data/raw/'

def open_data(filepath):
    with open(filepath) as f:
        table = pd.read_table(f, sep=' ', index_col=0, header=None,   lineterminator='\n')
        
    return table

def ensemble_mean(data,name):
    mean = np.zeros(len(data[1]))
    for i in range(9):
        mean += data[i+2]
    
    data['ens_mean'] = mean/9
    data.columns = ['obs', name+'_1', name+'_2', name+'_3',name+'_4', name+'_5', name+'_6',name+'_7', name+'_8', name+'_9','ens_mean']
    return data

def great_ensemble(data_list,name_list):
    df = pd.DataFrame({'obs':data_list[0][1]})
    df.index = data_list[0].index
    for data,name in zip(data_list,name_list):
        data.columns = ['obs', name+'_1', name+'_2', name+'_3',name+'_4', name+'_5', name+'_6',name+'_7', name+'_8', name+'_9']
        df = df.merge(data)
        
    mean = np.zeros(len(df['obs']))
    for i in range(27):
        mean += df.iloc[:,i+1]

    df['ens_mean'] = mean / 27
    return df

def obs_vs_ensmean(data,name):
    plt.plot(data['obs'],data['obs'],'--k')
    plt.scatter(data['obs'],data['ens_mean'],marker='o',color='r')
    plt.title(name)
    plt.xlabel('Observations'); plt.ylabel('Forecast')
    
    
N = 27 #Ensemble members
def categorization_terciles(df):
    terciles = df['obs'].quantile([0.33,0.66,0.99]).values
    categories = np.where(df['obs'] <= terciles[0],1,0)*(-1) + np.where(df['obs'] >= terciles[2],1,0)
    for i in range(N): 
        categories = np.where(df.iloc[:,i+2] <= terciles[0],1,0)*(-1) + np.where(df.iloc[:,i+2] >= terciles[2],1,0)
        df[df.columns[i+2]+'_cat'] = categories
        
    return df
    

