
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# Download latest version
car_data = kagglehub.dataset_download("nehalbirla/vehicle-dataset-from-cardekho")

print("Path to dataset files:", car_data)


# Define the path to the CSV file

file_path = car_data + '/Car data.csv' 
data = pd.read_csv(file_path) 
print(data)
# using ai to help me pick a perticular data 
# Filter the DataFrame to show only cars with a selling price >= 5 lakhs
#print(data[data['Selling_Price'] >= 5.02])
print(data[data["Year"] == 2014])

plt.scatter(data["Year"], data["Selling_Price"])
plt.title("Data set from Kaggel")
plt.xlabel("Year ")
plt.ylabel("Selling price")
plt.show()