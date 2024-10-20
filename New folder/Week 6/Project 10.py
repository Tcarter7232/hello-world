def calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours):
    # calculate regular pay
    regular_pay = hourly_wage * regular_hours
    # calculate overtime pay (1.5 times the hourly wage)
    overtime_pay = overtime_hours * (1.5 * hourly_wage)
    # total pay is regular pay plus overtime pay
    total_pay = regular_pay + overtime_pay
    return total_pay

hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the total regular hours worked: "))
overtime_hours = float(input("Enter the total overtime hours worked: "))

# Calculate the total weekly pay
total_weekly_pay = calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours)

print(f"Total weekly pay: ${total_weekly_pay:.2f}")
