import sys as _sys
_sys.path.append('../')
import pandas as pd
import matplotlib.pyplot as plt


def plot_line_chart(df, operationType, groupByList, returnField, title = "Title", xLabel = "xLabel", yLabel = "yLabel"):

    if operationType == "mean":
        life_by_cont = df.groupby(groupByList)[returnField].mean().unstack()
    
    plt.figure(figsize=(10,5))

    for cont in life_by_cont.columns:
        plt.plot(life_by_cont.index, life_by_cont[cont], label=cont)

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.show()

def plot_scatter_chart (df, operationType, groupByList, returnField, title = "Title", xLabel = "xLabel", yLabel = "yLabel"):
    plt.show() #em desenvolvimento