import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set up streamlit app title
st.title('Solar Farm Data Analysis')

# Load datasets
benin_data = pd.read_csv('../ata/benin-malanville.csv')
sierraleone_data = pd.read_csv('../data/sierraleone-bumbuna.csv')
togo_data = pd.read_csv('../data/togo-dapaong_qc.csv')

# sidebar for selecting dataset
dataset=st.sidebar.selectbox('select Dataset',('benin','sierraleone','togo'))

# Display selected dataset
if dataset == 'benin':
    data =benin_data
elif dataset == 'sierraleone':
    data=sierraleone_data
else:
    data=togo_data

st.write(data.describe())

# plotting GHI Distribution 
st.subheader('GHI Distribution')
fig, ax = plt.subplots()
sns.histplot(data['GHI'],kde=True, ax=ax)
st.pyplot(fig)

# plot correlation Heatmap
st.subheader('correlation Heatmap')
corr=data[['GHI','DNI','DHI','Tamb','RH','WS','WSgust','BP']].corr()
fig,ax=plt.subplots(figsize=(10,8))
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f',linewidths=.5,ax=ax)
st.pyplot(fig)

# Time Series Analaysis
st.subheader('Time Series Analysis')
data['Timestamp']=pd.to_datetime(data['Timestamp'])
data.set_index('Timestamp',inplace=True)

fig, ax=plt.subplots(figsize=(12,6))
ax.plot(data.index,data['GHI'],label='GHI')
ax.plot(data.index,data['DNI'],label='DNI',linestyle='--')
ax.plot(data.index,data['DHI'],label='DHI',linestyle=':')
ax.set_xlabel('Date')
ax.set_ylabel('Radiance(W/m²)')
ax.set_title('Time series of solar radiation')
ax.legend()
st.pyplot(fig)