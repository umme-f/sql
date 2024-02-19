import pandas as pd

# Load the Excel file into a pandas DataFrame
excel_file_path = 'your_excel_file.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file_path)

# Define the time range you want to remove
start_time = '08:00:00'
end_time = '17:00:00'

# Convert the 'Time' column to timedelta format
df['Time'] = pd.to_timedelta(df['Time'])

# Create a mask to filter rows within the specified time range
mask = (df['Time'] < start_time) | (df['Time'] > end_time)

# Apply the mask to the DataFrame to keep rows outside the specified time range
df_filtered = df[mask]

# Save the modified DataFrame back to Excel
df_filtered.to_excel('filtered_excel_file.xlsx', index=False)


# =========== Sol 1==============
import pandas as pd

# Load the Excel file into a pandas DataFrame
excel_file_path = 'your_excel_file.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file_path)

# Define the time range you want to remove
start_time = '08:00:00'
end_time = '17:00:00'

# Convert the 'DateTime' column to datetime format
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Extract the time component from the datetime
df['Time'] = df['DateTime'].dt.time

# Create a mask to filter rows within the specified time range
mask = (df['Time'] < pd.to_datetime(start_time).time()) | (df['Time'] > pd.to_datetime(end_time).time())

# Apply the mask to the DataFrame to keep rows outside the specified time range
df_filtered = df[~mask]

# Save the modified DataFrame back to Excel
df_filtered.to_excel('filtered_excel_file.xlsx', index=False)



# =============Sol 2 ===================
import pandas as pd

# Load the Excel file into a pandas DataFrame
excel_file_path = 'your_excel_file.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file_path)

# Assuming your combined date-time column is named 'DateTime'
# Convert the 'DateTime' column to datetime format
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Define the time range you want to remove
start_time = pd.Timestamp('08:00:00').time()  # Replace with your start time
end_time = pd.Timestamp('17:00:00').time()    # Replace with your end time

# Create a mask to filter rows outside the specified time range
mask = (df['DateTime'].dt.time < start_time) | (df['DateTime'].dt.time > end_time)

# Apply the mask to the DataFrame to keep rows outside the specified time range
df_filtered = df[mask]

# Save the modified DataFrame back to Excel
df_filtered.to_excel('filtered_excel_file.xlsx', index=False)
