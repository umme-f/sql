import pandas as pd

# Read the CSV file
file_path = 'your_file.csv'  # Replace 'your_file.csv' with the actual file path
df = pd.read_csv(file_path)

# Change column names
column_name_mapping = {
    'old_col_name1': 'new_col_name1',
    'old_col_name2': 'new_col_name2',
    # Add more columns as needed
}
df.rename(columns=column_name_mapping, inplace=True)

# Convert 'Timestamp' column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Convert 'Timestamp' to string
df['Timestamp_str'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Split the DataFrame into two based on a condition (for example, time greater than noon)
condition = df['Timestamp'].dt.hour >= 12
df['Timestamp_greater_than_noon'] = df['Timestamp'][condition]
df['Timestamp_less_than_noon'] = df['Timestamp'][~condition]

# Save the split columns to new columns
df['Timestamp_greater_than_noon_str'] = df['Timestamp_greater_than_noon'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['Timestamp_less_than_noon_str'] = df['Timestamp_less_than_noon'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Remove rows based on a given time range (for example, keep only rows between 2 PM and 4 PM)
start_time = pd.to_datetime('14:00:00')
end_time = pd.to_datetime('16:00:00')

df = df[(df['Timestamp'] >= start_time) & (df['Timestamp'] <= end_time)]

# Drop unnecessary columns if needed
df.drop(['Timestamp_greater_than_noon', 'Timestamp_less_than_noon'], axis=1, inplace=True)

# Save the modified DataFrame back to a new CSV file or overwrite the existing one
output_file_path = 'modified_file.csv'  # Replace 'modified_file.csv' with the desired output file path
df.to_csv(output_file_path, index=False)

print(f"All tasks completed. Modified CSV file saved to: {output_file_path}")
