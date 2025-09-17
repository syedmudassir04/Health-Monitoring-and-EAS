import logging_config  # This makes sure the logging setup is applied first
import logging  # Then you import the logging module

# Now, you can log your messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("fkkkkk This is a critical message")

print("Logging test completed. Check the app.log file in the Logging folder.")
