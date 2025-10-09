import sys as _sys
_sys.path.append('../')
import pandas as pd
import matplotlib.pyplot as plt

def plot_average_life_expectancy_by_continent(df):
    life_by_cont = df.groupby(['year','continent'])['lifeExp'].mean().unstack()
    plt.figure(figsize=(10,5))
    for cont in life_by_cont.columns:
        plt.plot(life_by_cont.index, life_by_cont[cont], label=cont)
    plt.title('Média da Expectativa de Vida por Continente')
    plt.xlabel('Ano')
    plt.ylabel('Expectativa de Vida (anos)')
    plt.legend()
    plt.show()


def plot_average_per_capita_income_by_continent(df):
    life_by_cont = df.groupby(['year','continent'])['gdpPercap'].mean().unstack()
    plt.figure(figsize=(10,5))
    for cont in life_by_cont.columns:
        plt.plot(life_by_cont.index, life_by_cont[cont], label=cont)
    plt.title('Média do Renda Per Capita Por Continente')
    plt.xlabel('Ano')
    plt.ylabel('Renda Per Capita')
    plt.legend()
    plt.show()

def plot_total_population_by_continent(df):
    life_by_cont = df.groupby(['year','continent'])['pop'].mean().unstack()
    plt.figure(figsize=(10,5))
    for cont in life_by_cont.columns:
        plt.plot(life_by_cont.index, life_by_cont[cont], label=cont)
    plt.title('Média Populacional por Continente')
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.legend()
    plt.show()