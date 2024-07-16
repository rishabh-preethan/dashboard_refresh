# main.py

"""
Main entry point for the widget refresh application.

This script performs an initial refresh of all widgets and schedules daily refreshes.
"""

from refresh_logic import refresh_all_widgets
from scheduler import schedule_refresh
import configparser

# Load constants from the properties file
config = configparser.ConfigParser()
config.read('constants.properties')

TIME_REFRESH_SCHEDULE = config.get('DEFAULT', 'TIME_REFRESH_SCHEDULE')

if __name__ == "__main__":
    # Initial refresh before scheduling
    print("Performing initial refresh...")
    refresh_all_widgets()
    
    # Schedule daily refresh
    schedule_refresh(TIME_REFRESH_SCHEDULE)
