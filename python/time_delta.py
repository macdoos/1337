from datetime import datetime

# Function to calculate the absolute difference between two timestamps
def calculate_time_difference(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    
    # Convert both times to datetime objects
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    
    # Calculate the absolute difference in seconds
    diff = abs((dt1 - dt2).total_seconds())
    
    return int(diff)

# Hardcoded test case inputs as a list
test_cases = [
    ("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"),
    ("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000")
]

# Number of test cases
n = len(test_cases)

# Loop through the test cases and calculate the time difference
for t1, t2 in test_cases:
    result = calculate_time_difference(t1, t2)
    print(result)

