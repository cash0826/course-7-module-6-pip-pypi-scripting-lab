from datetime import datetime
import os

log_data = ["User logged in", "User updated profile", "Report exported"]
# filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input data must be a list of log entries.")
    
    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    try:
        with open(filename, "a") as file:
            for line in data:
                file.write(f"{line}\n")
    except FileNotFoundError:
        print(f"Error: The file {filename} could not be created.")
    
    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    
    return filename

def main():
    generate_log(log_data)

if __name__ == "__main__":
    main()