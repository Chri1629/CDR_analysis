import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--output', type=str, required=True, help="Inserire la directory corrente")
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
    ax.set_title('Distribuzione del CDR', fontsize=30)
    ax.set_xlabel('Classe', fontsize=30)
    ax.set_ylabel('Conteggi', fontsize=30)
    plt.show()
    fig.savefig(args.output + '/bar_plot.png', bbox_inches='tight', dpi = 600)

def quality():
    dati = pd.read_csv("oasis_merge.csv")
    print(dati.head())
    data = dati['CDR']
    print(data)
    bar_plot(data)

quality()
    
