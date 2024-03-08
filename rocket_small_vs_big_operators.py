import pandas as pd

# Load the CSV file
file_path = "rocket_staking_snapshot_2_removed_zeros.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Sort the data based on the 'value' column
data = data.sort_values(by="provided_eth", ascending=False)

# Filter data for datapoints with 'provided_eth' values less than or equal to 15
datapoints_below_15 = data[data["provided_eth"] <= 15]

# Calculate total sum, mean, and median for datapoints below or equal to 15
total_sum_below_15 = datapoints_below_15["provided_eth"].sum()
total_mean_below_15 = datapoints_below_15["provided_eth"].mean()
total_median_below_15 = datapoints_below_15["provided_eth"].median()

# Calculate overall total sum, mean, and median for the entire dataset
total_sum = data["provided_eth"].sum()
total_mean = data["provided_eth"].mean()
total_median = data["provided_eth"].median()

# Count total number of datapoints
total_datapoints = len(data)

# Count how many datapoint values are larger than 15
datapoints_above_15_count = data[data["provided_eth"] > 15].shape[0]

# Count how many datapoint values are below or equal to 15
datapoints_below_15_count = len(datapoints_below_15)

# Print the results for the entire dataset
print(f"Total Sum: {total_sum}")
print(f"Total Mean: {total_mean}")
print(f"Total Median: {total_median}")
print(f"Total datapoints: {total_datapoints}")
print(f"Datapoints with value larger than 15: {datapoints_above_15_count}")

# Print the results for datapoints below or equal to 15
print(f"Sum for datapoints <= 15: {total_sum_below_15}")
print(f"Mean for datapoints <= 15: {total_mean_below_15}")
print(f"Median for datapoints <= 15: {total_median_below_15}")
print(f"Datapoints with value <= 15: {datapoints_below_15_count}")
