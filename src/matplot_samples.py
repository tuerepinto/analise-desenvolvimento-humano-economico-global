import sys as _sys
_sys.path.append('../')
import pandas as pd
import matplotlib.pyplot as plt


def plot_line_chart(df, group, title = "Title", xLabel = "xLabel", yLabel = "yLabel"):
    plt.figure(figsize=(10,5))
    for cont in group.columns:
        plt.plot(group.index, group[cont], label=cont)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.show()

def plot_scatter_chart (df, xData, yData, title = "Title", xLabel = "xLabel", yLabel = "yLabel", showGrid = True):
    plt.figure(figsize=(10, 6))
    plt.scatter(xData, yData, alpha=0.6)
    plt.title(title)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.grid(showGrid)
    plt.show()

def scatter_subplots(df, 
                     dfPrincipalFieldName,  
                     dfXColFieldName,
                     dfYColFieldName,
                     nRows, 
                     nCols, 
                     dataToAnalyze, 
                     x_colLabel='lifeExp', 
                     y_colLabel='gdpPercap', 
                     cores=None, 
                     titulo_geral=None):
    fig, axs = plt.subplots(nRows, nCols, figsize=(14,10), constrained_layout=True)
    axs = axs.flatten()  # transformar em array 1D para fácil iteração

    if cores is None:
        cores = plt.cm.tab10.colors
    
    for i, value in enumerate(dataToAnalyze):
        color = cores[i % len(cores)]
        sub_df = df[df[dfPrincipalFieldName] == value]
        axs[i].scatter(sub_df[dfXColFieldName], sub_df[dfYColFieldName], alpha=0.6, color=color)
        axs[i].set_title(value)
        axs[i].set_xlabel(x_colLabel)
        axs[i].set_ylabel(y_colLabel)
        axs[i].grid(True)

    if titulo_geral:
        fig.suptitle(titulo_geral, fontsize=16)
    
    plt.show()