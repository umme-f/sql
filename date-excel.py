import pandas as pd
import numpy as np

# Load the Excel file into a pandas DataFrame
file_path = r'Book1.xlsx'
df = pd.read_excel(file_path)

# Assuming your DataFrame has a column named 'Date' containing datetime values
df['Date'] = pd.to_datetime(df['Date'])

# Identify weekends (Saturday and Sunday)
weekend_mask = (df['Date'].dt.dayofweek == 5) | (df['Date'].dt.dayofweek == 6)

# Filter out weekends
df = df[~weekend_mask]

# Save the modified DataFrame back to the Excel file
df.to_excel('output_file.xlsx', index=False)
