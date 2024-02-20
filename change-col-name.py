# ======================= To change csv col name using python ========================

import pandas as pd

# Read the CSV file
file_path = 'your_file.csv'  # Replace 'your_file.csv' with the actual file path
df = pd.read_csv(file_path)

# Define a dictionary to map old column names to new column names
column_name_mapping = {
    'old_col_name1': 'new_col_name1',
    'old_col_name2': 'new_col_name2',
    # Add more columns as needed
}

# Rename columns using the rename() function
df.rename(columns=column_name_mapping, inplace=True)

# Save the modified DataFrame back to a new CSV file or overwrite the existing one
output_file_path = 'modified_file.csv'  # Replace 'modified_file.csv' with the desired output file path
df.to_csv(output_file_path, index=False)

print(f"Columns in the CSV file have been renamed. New CSV file saved to: {output_file_path}")
