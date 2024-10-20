def is_equilateral(a, b, c):
    """Returns True if the triangle with sides a, b, c is equilateral, False otherwise."""
    if a == b == c:
        return True
    else:
        return False

def main():
    while True:
        try:
            a = float(input("Enter the length of side a: "))
            b = float(input("Enter the length of side b: "))
            c = float(input("Enter the length of side c: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if is_equilateral(a, b, c):
        print("The triangle is equilateral.")
    else:
        print("The triangle is not equilateral.")

if __name__ == "__main__":
    main()
