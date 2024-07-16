# scheduler.py

import schedule
import time
from datetime import datetime
from refresh_logic import refresh_all_widgets
import configparser

# Load constants from the properties file
config = configparser.ConfigParser()
config.read('constants.properties')

TIME_REFRESH_SCHEDULE = config.get('DEFAULT', 'TIME_REFRESH_SCHEDULE')

def get_local_time():
    """
    Get the current local time of the server.

    Returns:
    - str: Current local time in HH:MM format.
    """
    return datetime.now().strftime('%H:%M')

def schedule_refresh(time_refresh_schedule):
    """
    Schedule the refresh of all widgets at a specified time daily.

    Parameters:
    - time_refresh_schedule (str): The time (HH:MM) to perform the daily refresh.

    This function uses the `schedule` module to run `refresh_all_widgets` at the specified time.
    """
    print(f"Scheduling refresh at {time_refresh_schedule} local time")

    schedule.every().day.at(time_refresh_schedule).do(refresh_all_widgets)

    # Print statement indicating scheduler has started
    print(f"Scheduler started. Waiting for scheduled refresh at {time_refresh_schedule} local time...")

    while True:
        current_time = get_local_time()
        print(f"Checked at {current_time} local time")
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_refresh(TIME_REFRESH_SCHEDULE)
