import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)
def plot_histogram(data,column,title="Histogram",xlabel="Value", ylabel="Frequency", kde=True):
    fig,ax=plt.subplots()
    sns.histplot(data[column],kde=kde,ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def plot_correlation_heatmap(data,columns,title="correlation Heatmap", cmap='coolwarm'):
    corr = data[columns].corr()
    fig,ax=plt.subplots(figsize=(10, 8))
    sns.heatmap(corr,annot=True,cmap=cmap,fmt='.2f',linewidths=.5,ax=ax)
    ax.set_title(title)
    return fig

def perform_time_series_analysis(data,columns,title="Time series Analysis",ylabel="Radiance (W/m²)"):
    fig, ax=plt.subplots(figsize=(12,6))
    for column in columns:
        ax.plot(data.index,data[column],label=column)
    ax.set_xlabel('Date')
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    return fig
def preprocess_data(data):
    data['Timestamp']=pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp',inplace=True)
    return data