# Constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Get user input
grossIncome = float(input("Enter your gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Calculate total deductions
totalDeductions = STANDARD_DEDUCTION + numDependents * DEPENDENT_DEDUCTION

# Calculate taxable income
taxableIncome = grossIncome - totalDeductions

# Calculate total tax owed
totalTaxOwed = taxableIncome * TAX_RATE

# Print the result
print("Total tax owed: ${:.2f}".format(totalTaxOwed))
