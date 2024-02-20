# ================ To remove a range of columns from a CSV file using Python ==============
import pandas as pd

# Create a sample DataFrame
data = {'Timestamp': ['2024-02-20 12:30:45', '2024-02-20 14:15:30', '2024-02-20 16:45:00'],
        'Value': [10, 20, 15]}

df = pd.DataFrame(data)

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

# Display the results
print("Original DataFrame:")
print(df)
