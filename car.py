
import kagglehub
import pandas as pd

# Download latest version
car_data = kagglehub.dataset_download("nehalbirla/vehicle-dataset-from-cardekho")

print("Path to dataset files:", car_data)


# Define the path to the CSV file

file_path = car_data + '/CAR DETAILS FROM CAR DEKHO.csv' # Ensure this matches the actual file name in the dataset # Load the dataset into a DataFrame 
data = pd.read_csv(file_path) # Print the DataFrame
print(data)


