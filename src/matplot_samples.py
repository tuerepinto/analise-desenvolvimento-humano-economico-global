import sys as _sys
_sys.path.append('../')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_line_chart(group,  
                    title = "Title",
                    xLabel = "xLabel", 
                    yLabel = "yLabel", 
                    showGrid = True, 
                    marker='o',
                    xSize=10,
                    ySize=5):
    
    figsize=(xSize,ySize)
    plt.figure(figsize=figsize)
    for cont in group.columns:
        plt.plot(group.index, group[cont], label=cont, marker=marker)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.grid(showGrid)
    plt.show()

def plot_scatter_chart (xData, yData, title = "Title", xLabel = "xLabel", yLabel = "yLabel", showGrid = True):
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
                     xLabel='lifeExp', 
                     yLabel='gdpPercap', 
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
        axs[i].set_xlabel(xLabel)
        axs[i].set_ylabel(yLabel)
        axs[i].grid(True)

    if titulo_geral:
        fig.suptitle(titulo_geral, fontsize=16)
    
    plt.show()