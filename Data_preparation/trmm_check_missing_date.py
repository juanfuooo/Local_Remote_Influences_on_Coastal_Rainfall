import os
import re
import glob
from datetime import datetime, timedelta

# Directory containing your nc files
data_dir = r"C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation\TRMM"  # Update this path

# Pattern to match your nc files
file_pattern = '3B42_Daily.*.7.nc4'

# Get a list of all files matching the pattern
file_list = glob.glob(os.path.join(data_dir, file_pattern))
print(f"Found {len(file_list)} files")

# Function to extract date from filename
def extract_date(filename):
    # Extract the date part from the filename (e.g., '19980101' from '3B42_Daily.19980101.7.nc4')
    match = re.search(r'3B42_Daily\.(\d{8})\.7\.nc4', os.path.basename(filename))
    if match:
        date_str = match.group(1)
        # Convert to datetime
        try:
            return datetime.strptime(date_str, '%Y%m%d')
        except ValueError:
            print(f"Warning: Invalid date format in {filename}")
            return None
    return None

# Extract dates from all filenames
existing_dates = set()
invalid_files = []

for file_path in file_list:
    date = extract_date(file_path)
    if date:
        existing_dates.add(date.strftime('%Y%m%d'))
    else:
        invalid_files.append(os.path.basename(file_path))

if invalid_files:
    print(f"Warning: Could not extract dates from {len(invalid_files)} files")
    for file in invalid_files[:10]:  # Show first 10 invalid files
        print(f"  - {file}")
    if len(invalid_files) > 10:
        print(f"  ... and {len(invalid_files) - 10} more")

# Generate all dates that should exist in the range
start_date = datetime(1998, 1, 1)
end_date = datetime(2019, 12, 30)
expected_dates = set()

current_date = start_date
while current_date <= end_date:
    expected_dates.add(current_date.strftime('%Y%m%d'))
    current_date += timedelta(days=1)

# Find missing dates
missing_dates = expected_dates - existing_dates

print(f"\nExpected {len(expected_dates)} dates from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
print(f"Found {len(existing_dates)} dates in files")
print(f"Missing {len(missing_dates)} dates")

# Display missing dates
if missing_dates:
    print("\nMissing dates:")
    
    # Convert back to datetime for sorting
    missing_dates_list = [datetime.strptime(date_str, '%Y%m%d') for date_str in missing_dates]
    missing_dates_list.sort()
    
    for date in missing_dates_list:
        print(f"  - {date.strftime('%Y-%m-%d')} (3B42_Daily.{date.strftime('%Y%m%d')}.7.nc4)")

    # Check for consecutive missing dates
    consecutive_dates = []
    current_group = []
    
    for i in range(len(missing_dates_list)):
        if i == 0:
            current_group.append(missing_dates_list[i])
        elif (missing_dates_list[i] - missing_dates_list[i-1]).days == 1:
            current_group.append(missing_dates_list[i])
        else:
            if len(current_group) > 1:
                consecutive_dates.append(current_group)
            current_group = [missing_dates_list[i]]
    
    if len(current_group) > 1:
        consecutive_dates.append(current_group)
    
    if consecutive_dates:
        print("\nConsecutive missing dates:")
        for group in consecutive_dates:
            start = group[0].strftime('%Y-%m-%d')
            end = group[-1].strftime('%Y-%m-%d')
            print(f"  - {start} to {end} ({len(group)} days)")

# Check if any unexpected dates exist (dates outside the expected range)
unexpected_dates = existing_dates - expected_dates
if unexpected_dates:
    print(f"\nFound {len(unexpected_dates)} dates outside the expected range")
    
    # Convert to datetime for sorting
    unexpected_dates_list = [datetime.strptime(date_str, '%Y%m%d') for date_str in unexpected_dates]
    unexpected_dates_list.sort()
    
    # Show first few and last few
    max_display = 10
    if len(unexpected_dates_list) <= max_display * 2:
        for date in unexpected_dates_list:
            print(f"  - {date.strftime('%Y-%m-%d')}")
    else:
        for date in unexpected_dates_list[:max_display]:
            print(f"  - {date.strftime('%Y-%m-%d')}")
        print(f"  ... {len(unexpected_dates_list) - 2*max_display} more dates ...")
        for date in unexpected_dates_list[-max_display:]:
            print(f"  - {date.strftime('%Y-%m-%d')}")