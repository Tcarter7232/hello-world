def calculate_minutes(years):
    # 1 year = 365 days, 1 day = 24 hours, 1 hour = 60 minutes
    minutes_per_year = 365 * 24 * 60
    minutes = years * minutes_per_year
    return minutes

years = int(input("Enter the number of years: "))
minutes = calculate_minutes(years)
print(f"Number of minutes in {years} years is: {minutes}")
