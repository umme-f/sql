import pandas as pd
from datetime import date 
import holidays 


# Load the Excel file into a pandas DataFrame
file_path = r'Book1.xlsx'
df = pd.read_excel(file_path)

# Assuming your DataFrame has a column named 'Date' containing datetime values
df['Date'] = pd.to_datetime(df['Date'])

# Identify weekends (Saturday and Sunday)
weekend_mask = (df['Date'].dt.dayofweek == 5) | (df['Date'].dt.dayofweek == 6)
df = df[~weekend_mask]

# Select country 
jp_holidays = holidays.Japan() 

####################### For holidays other than weekends ####################
for ptr in holidays.Japan(years = 2023).items(): 
	print(ptr) 

    # df=df[~ptr]



# Save the modified DataFrame back to the specified Excel file
df.to_excel('output_file.xlsx', index=False)
