import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Download latest version of the dataset
path = kagglehub.dataset_download("nehalbirla/vehicle-dataset-from-cardekho")
print("Path to dataset files:", path)

# Load the dataset
file_path = path + '/CAR DETAILS FROM CAR DEKHO.csv'  # Adjust the filename if necessary
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Basic Seaborn plot to verify everything is working
plt.figure(figsize=(10, 6))
sns.histplot(df['selling_price'], kde=True)
plt.title('Selling Price Distribution')
plt.xlabel('Selling Price')
plt.ylabel('Frequency')
plt.show()

# Additional Plotly visualization
fig = px.scatter(df, x='year', y='selling_price', color='fuel', title='Selling Price by Year and Fuel Type')
fig.show()
