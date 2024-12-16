from datetime import datetime

# Set the current local time as specified
current_time = datetime.fromisoformat('2024-12-15T08:09:39+05:30')

# Example function to display the current time

def display_time():
    print(f'The current local time is: {current_time}')

# Run the function
if __name__ == '__main__':
    display_time()
