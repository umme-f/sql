from datetime import datetime

# Assuming the numeric value is the number of milliseconds since the Unix epoch
numeric_value_milliseconds = 1613795367000  # Replace this with your numeric value

# Convert numeric value to a datetime object
timestamp = datetime.utcfromtimestamp(numeric_value_milliseconds / 1000.0)

print("Timestamp:", timestamp)
