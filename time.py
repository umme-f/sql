from datetime import date 
import holidays 

# Select country 
jp_holidays = holidays.Japan() 

# Print all the holidays in UnitedKingdom in year 2018 
for ptr in holidays.Japan(years = 2023).items(): 
	print(ptr) 

