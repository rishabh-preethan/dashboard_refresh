import schedule
import time
import logging
import subprocess
from datetime import datetime
from config import REFRESH_TIME

# Configure logging
# logging.basicConfig(
#     filename='//home//rishabhp//sandbox//Final_Customer_Dashboard//app.log',  # Path to the log file
#     filemode='a',  # Append mode
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
#     level=logging.INFO  # Log level
# )

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def refresh_all_widgets():
    """
    Function to refresh all widgets by calling subprocesses for base and owner query refresh.
    """
    try:
        logging.info("Starting widget refresh...")
        subprocess.run(["python3", "base_query_refresh.py"])
        # Add more subprocess calls if needed
        logging.info("Widget refresh completed.")
    except Exception as e:
        logging.error(f"Error in refreshing widgets: {e}")

def schedule_refresh(time_refresh_schedule):
    """
    Schedule the refresh of all widgets at a specified time daily.

    Parameters:
    - time_refresh_schedule (str): The time (HH:MM) in local time to perform the daily refresh.
    """
    try:
        logging.info(f"Scheduling refresh at {time_refresh_schedule} local time")

        # Schedule refresh at the specified local time
        schedule.every().day.at(time_refresh_schedule).do(refresh_all_widgets)
        
        logging.info("Scheduler started. Waiting for scheduled refresh...")

        while True:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"Current local time: {current_time}")
            schedule.run_pending()
            time.sleep(60)
    except Exception as e:
        logging.error(f"Error in scheduling refresh: {e}")

if __name__ == "__main__":
    try:
        logging.info("Starting scheduler...")
        schedule_refresh(REFRESH_TIME)
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
