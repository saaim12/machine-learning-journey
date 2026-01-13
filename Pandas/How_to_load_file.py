import pandas as pd
# Load a CSV file into a DataFrame
df = pd.read_csv('Mercedes_Company_dataset.csv')
print(df.head())
# Display basic information about the DataFrame
print(df.info())
# Display summary statistics of the DataFrame
print(df.describe())
 
