import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Load the dataset
df = pd.read_csv('all_stocks_5yr.csv')
#print(df.head())
print(df.info())

print(df.isnull().sum())

#drop nan rows
df = df.dropna()

df['date'] = pd.to_datetime(df['date'])
print(df.duplicated().sum())

df.drop_duplicates(keep=False, inplace=True)
df['date'] = pd.to_datetime(df['date'])

df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'}, inplace=True)
df.drop(['High', 'Low', 'Volume'], axis=1, inplace=True)

q1 = df['Close'].quantile(0.25)
q3 = df['Close'].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
df = df[df['Close'] <= upper_bound]


plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='Close', data=df)
plt.title('Closing Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Stock Price')
plt.show()

df['year'] = df['date'].dt.year
sns.boxplot(x='year', y='close', data=df)
plt.title('Closing Stock Prices by Year')
plt.xlabel('Year')
plt.ylabel('Closing Stock Price')
plt.show()