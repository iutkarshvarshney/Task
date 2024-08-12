import json
from datetime import datetime

# Load the JSON data from a file
with open('NIFTYoption_chain.json', 'r') as file:
    data = json.load(file)

# Function to find the latest date in a given date dictionary
def find_latest_date(date_dict):
    # Convert the date strings to datetime objects
    datetime_items = [(key, datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S%z')) for key, date_str in date_dict.items()]
    # Find the latest date
    latest_entry = max(datetime_items, key=lambda item: item[1])
    return latest_entry[0]  # Return the key of the latest date

# Process each top-level key in the JSON data
filtered_data = {}
for main_key, main_value in data.items():
    if isinstance(main_value, dict) and "data" in main_value:
        date_data = main_value["data"].get("date")
        if date_data and isinstance(date_data, dict):
            latest_date_key = find_latest_date(date_data)
            # Store only the latest date's data
            filtered_data[main_key] = {
                "strike_price": main_value.get("strike_price"),
                "ot": main_value.get("ot"),
                "data": {"date": {latest_date_key: date_data[latest_date_key]}}
            }

# Save the filtered data back to a JSON file
with open('filtered_data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)

print("Filtered data saved to 'filtered_data.json'.")
