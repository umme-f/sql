#To remove a range of columns from a CSV file using Python 
import pandas as pd

# Read the CSV file
file_path = 'your_file.csv'  # Replace 'your_file.csv' with the actual file path
df = pd.read_csv(file_path)

# Define the range of columns to be removed
start_col = 2  # Replace with the starting column index (0-based) to be removed
end_col = 5    # Replace with the ending column index (exclusive) to be removed

# Remove columns using iloc
df.drop(df.columns[start_col:end_col], axis=1, inplace=True)

# Save the modified DataFrame back to a new CSV file or overwrite the existing one
output_file_path = 'modified_file.csv'  # Replace 'modified_file.csv' with the desired output file path
df.to_csv(output_file_path, index=False)

print(f"Range of columns removed. New CSV file saved to: {output_file_path}")
