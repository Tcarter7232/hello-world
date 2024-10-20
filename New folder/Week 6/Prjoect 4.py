def calculate_distance(initial_height, num_bounces):
    total_distance = initial_height
    bounce_height = initial_height
    
    for _ in range(num_bounces + 1):
        total_distance += bounce_height * 2
        bounce_height *= 0.6
    
    return total_distance

initial_height = float(input("Enter the initial height from which the ball is dropped (in feet): "))
num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

total_distance = calculate_distance(initial_height, num_bounces)

print(f"The total distance traveled by the ball is {total_distance:.2f} feet.")
