import pandas as pd

# Load the CSV file
file_path = "lido_stakers_balances.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Sort the data based on the 'value' column
data = data.sort_values(by="value", ascending=False)

# Calculate total sum, mean, and median for the entire dataset
total_sum = data["value"].sum()
total_mean = data["value"].mean()
total_median = data["value"].median()


def print_percentile_stats(start_percentile, end_percentile, step):
    cumulative_sum_ratio = 0  # Initialize cumulative sum ratio

    for percentile in range(start_percentile, end_percentile, step):
        lower_bound = data["value"].quantile(percentile / 100.0)
        upper_bound = data["value"].quantile((percentile + step) / 100.0)

        values_in_percentile = data[
            (data["value"] <= upper_bound) & (data["value"] >= lower_bound)
        ]

        percentile_sum = values_in_percentile["value"].sum()
        percentile_mean = values_in_percentile["value"].mean()
        percentile_median = values_in_percentile["value"].median()
        percentile_std_err = values_in_percentile["value"].sem()

        sum_ratio = percentile_sum / total_sum
        cumulative_sum_ratio += sum_ratio  # Update cumulative sum ratio
        mean_ratio = percentile_mean / total_mean
        median_ratio = percentile_median / total_median

        print(f"Percentile {percentile}-{percentile + step}:")
        print(f"  First value: {values_in_percentile.iloc[0]['value']}")
        print(f"  Last value: {values_in_percentile.iloc[-1]['value']}")
        print(f"  Sum Ratio: {sum_ratio:.2f}")
        print(
            f"  Cumulative Sum Ratio: {cumulative_sum_ratio:.2f}"
        )  # Print cumulative sum ratio
        print(f"  Mean: {percentile_mean:.2e}")
        print(f"  Median: {percentile_median:.2e}")
        print(f"  Standard Error: {percentile_std_err:.2e}")
        print(f"  Mean Ratio: {mean_ratio:.2f}")
        print(f"  Median Ratio: {median_ratio:.2f}\n")


# Print stats for each 10-percentile range
print_percentile_stats(0, 100, 10)

# # Print stats for each individual percentile from 91 to 100
# print_percentile_stats(0, 100, 1)
