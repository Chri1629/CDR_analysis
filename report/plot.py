import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--output', type=str, required=True, help="Inserire la directory corrente", default="./")
args = parser.parse_args()


def bar_plot(data):
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

    plt.rc('font', **font)
    d = np.diff(np.unique(data)).min()
    left_of_first_bin = data.min() - float(d)/2
    fig, ax= plt.subplots(figsize=(15, 8))
    right_of_last_bin = data.max() + float(d)/2
    plt.hist(data, np.arange(left_of_first_bin, right_of_last_bin + d, d))
    ax.set_xticklabels(['0','0', '0.5', '1', '1.5', '2'],
                    rotation=0, fontsize=30)
    #ax.set_title('Distribuzione del CDR', fontsize=30)
    ax.set_xlabel('Classe', fontsize=30)
    ax.set_ylabel('Conteggi', fontsize=30)
    plt.show()
    fig.savefig(args.output + '/bar_plot.png', bbox_inches='tight', dpi = 600)

def scatter_plot(x, y):
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

    plt.rc('font', **font)
        
    fig = plt.figure(figsize=(15,8))
    coef = np.polyfit(x,y,1)
    poly1d_fn = np.poly1d(coef) 
    plt.plot(x,y, '+', color = (0.2,0.1,0.3))
    plt.plot(x, poly1d_fn(x), '--k', color = (0.7,0.1,0.3), label = "Regression line")
    
    plt.xticks( fontsize = 20)
    plt.yticks( fontsize = 20)
    plt.xlabel('eTIV', size = 35) 
    plt.ylabel('ASF', size = 35) 
    plt.legend(loc="best", prop={'size': 35})
    plt.show()
    plt.ioff()
    fig.savefig(args.output + '/scatter_plot.png', bbox_inches='tight', dpi = 600)

def quality():
    dati = pd.read_csv("oasis_longitudinal.csv")
    print(dati.head())
    data = dati['CDR']
    print(data)
    bar_plot(data)
    scatter_plot(dati['eTIV'], dati['ASF'])

quality()
    
