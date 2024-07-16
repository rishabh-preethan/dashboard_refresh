import datetime
import logging

logging.basicConfig(
    filename='//home//rishabhp//sandbox//Final_Customer_Dashboard//app_test.log',  # Path to the log file
    filemode='a',  # Append mode
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO  # Log level
)

def log_time():
    current_time = datetime.datetime.now()
    logging.info(f"{current_time}\n")
    # with open("/home/rishabhp/sandbox/Final_Customer_Dashboard/time_log.txt", "a") as file:
    #     current_time = datetime.datetime.now()
    #     file.write(f"{current_time}\n")

if __name__ == "__main__":
    log_time()
