import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load a dataset from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)
#clean the dataset by removing any rows with missing values
def clean_data(df):
    df.dropna(inplace=True)
    return df
# calculate the correlation matrix 
def calculate_correlation(df):
    return df[['GHI','DNI','DHI','Tamb','RH','WS','WSgust','BP']].corr()

# prepare the dataframe for the time series analysis
def prepare_time_series(df):
    df['Timestamp']=pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp',inplace=True)
    return df


def plot_ghi_distribution(data,country):
    sns.histplot(data['GHI'],kde=True)
    plt.title(f'GHI Distribution for {country}')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Frequency')
    plt.show()
def plot_correlation_heatmap(data,country):
    corr=data[['GHI','DNI','DHI','Tamb','RH','WS','WSgust','BP']].corr()
    sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f')
    plt.title(f'Correlation Heatmap for {country}')
    plt.show()
def plot_time_series(data,country):
    data['Timestamp']=pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp',inplace=True)

    plt.figure(figsize=(12,6))
    plt.plot(data.index,data['GHI'],label='GHI')
    plt.plot(data.index,data['DNI'],label='DNI',linestyle='--')
    plt.plot(data.index,data['DHI'],label='DHI',linestyle=':')
    plt.title(f'Time series of solar Radiation for {country}')
    plt.xlabel('Date')
    plt.ylabel('Radiance (W/m²)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("starting the script...")
    #load datasets
    benin_data = load_data('data/benin-malanville.csv')
    print("Loaded Benin data")
    sierraleone_data=load_data('data/sierraleone-bumbuna.csv')
    print("Loaded sierraleone data")
    togo_data=load_data('data/togo-dapaong_qc.csv')
    print("Loaded togo data")


    #clean datasets
    benin_data = clean_data(benin_data)
    print("cleaned Benin data")
    sierraleone_data=clean_data(sierraleone_data)
    print("cleaned sierraleone data")
    togo_data=clean_data(togo_data)
    print("cleaned togo data")

    #plotting
    plot_ghi_distribution(benin_data,'benin')
    print("plotted GHI Distribution for benin")
    plot_ghi_distribution(sierraleone_data,'sierraleone')
    plot_ghi_distribution(togo_data,'togo')

    plot_correlation_heatmap(benin_data,'benin')
    plot_correlation_heatmap(sierraleone_data,'sierraleone')
    plot_correlation_heatmap(togo_data,'togo')

    plot_time_series(benin_data,'benin')
    plot_time_series(sierraleone_data,'sierraleone')
    plot_time_series(togo_data,'togo')
   