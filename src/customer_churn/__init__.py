from datetime import datetime
import os
import sys
import logging

# Logfile name is defined using the current date and time
log_file_name = f'{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log'

# Assign path to the logfile
log_file_path = os.path.join(os.getcwd(),'logs', log_file_name)

# Create the log folder if not already created
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Configuration for the logger
logging.basicConfig(
    # Formatting the logs
    format = "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    handlers=[
        logging.FileHandler(log_file_path), # Output logs to the file 
        logging.StreamHandler(sys.stdout) # Output logs in the terminal/console
    ]

)

logger = logging.getlogger('customer-churn')