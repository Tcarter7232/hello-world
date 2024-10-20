def predict_population(initial_population, growth_rate, growth_period, total_hours):
    """
    Predicts the total population after a certain number of hours.

    Args:
        initial_population (int): The initial number of organisms.
        growth_rate (float): The rate of growth (a real number greater than 0).
        growth_period (float): The number of hours it takes to achieve the growth rate.
        total_hours (int): The total number of hours during which the population grows.

    Returns:
        int: The predicted total population.
    """
    if growth_rate <= 0:
        raise ValueError("Growth rate must be greater than 0")
    if growth_period <= 0:
        raise ValueError("Growth period must be greater than 0")

    num_growth_periods = total_hours // growth_period
    total_population = initial_population * (growth_rate ** num_growth_periods)
    return round(total_population)

# Input section with validation
try:
    initial_population = int(input("Enter the initial number of organisms: "))
    growth_rate = float(input("Enter the growth rate: "))
    growth_period = float(input("Enter the growth period (in hours): "))  # Changed to float
    total_hours = int(input("Enter the total number of hours: "))
    
    predicted_population = predict_population(initial_population, growth_rate, growth_period, total_hours)
    print(f"Predicted total population: {predicted_population:.0f}")
except ValueError as e:
    print(f"Invalid input: {e}")
