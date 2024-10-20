def get_filename(prompt):
    """Get a filename from the user."""
    while True:
        filename = input(prompt)
        try:
            # Check if the file exists
            with open(filename, 'r') as file:
                return filename
        except FileNotFoundError:
            print("File not found. Please try again.")

def copy_file(src_filename, dst_filename):
    """Copy the contents of the source file to the destination file."""
    try:
        with open(src_filename, 'r') as src_file:
            with open(dst_filename, 'w') as dst_file:
                dst_file.write(src_file.read())
        print(f"File '{src_filename}' copied to '{dst_filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Get the source and destination filenames from the user
    src_filename = get_filename("Enter the source filename: ")
    dst_filename = input("Enter the destination filename: ")

    # Copy the file
    copy_file(src_filename, dst_filename)

if __name__ == "__main__":
    main()
