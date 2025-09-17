import logging
import os

# Set up the Logging directory
log_directory = os.path.join(os.getcwd(), 'Logging')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Define the log file path
log_file = os.path.join(log_directory, 'app.log')

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,  # You can change the level (DEBUG, INFO, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Log to app.log inside the Logging folder
        logging.StreamHandler()         # Optionally log to console
    ]
)

# Log some messages

