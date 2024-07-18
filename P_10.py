# Define the number of seconds in a minute, minutes in an hour, and hours in a day
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24

# Define the number of days in a common year and a leap year
days_per_common_year = 365
days_per_leap_year = 366

# Calculate the number of seconds in a common year
seconds_per_common_year = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_common_year

# Calculate the number of seconds in a leap year
seconds_per_leap_year = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_leap_year

print(f"Number of seconds in a common year: {seconds_per_common_year}")
print(f"Number of seconds in a leap year: {seconds_per_leap_year}")
