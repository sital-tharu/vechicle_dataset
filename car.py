
import kagglehub
import pandas as pd

# Download latest version
car_data = kagglehub.dataset_download("nehalbirla/vehicle-dataset-from-cardekho")

print("Path to dataset files:", car_data)


# Define the path to the CSV file

file_path = car_data + '/Car data.csv' 
data = pd.read_csv(file_path) 
print(data)
# using ui to help me pick a perticular data 
# Filter the DataFrame to show only cars with a selling price >= 5 lakhs
print(data[data['Selling_Price'] >= 5.00])

# Display the filtered DataFrame



