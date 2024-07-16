# base_query_refresh.py

import logging
import subprocess
import time
import datetime
from utils import get_url, post_request, get_request
from config import BASE_QUERY_IDS, REFRESH_TIME

# BASE_QUERY_IDS = [307, 305, 303, 292, 259]
# REFRESH_TIME = "04:36"

# logging.basicConfig(
#     filename='//home//rishabhp//sandbox//Final_Customer_Dashboard//app.log',  # Path to the log file
#     filemode='a',  # Append mode
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
#     level=logging.INFO  # Log level
# )

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def refresh_widget(query_id):
    """
    Refreshes the widget for the given query ID.

    Args:
        query_id (int): The ID of the query to be refreshed.

    Description:
        This function sends a POST request to refresh the widget associated with the given query ID.
        It then polls the job status until the query result is updated.
    """
    logging.info(f"Starting refresh for query ID: {query_id}")
    payload = {
        "id": query_id,
        "parameters": {},
        "apply_auto_limit": True,
        "max_age": 0
    }
    results_url = get_url('queries', query_id) + '/results'
    response = post_request(results_url, payload)

    if response and "job" in response:
        job_id = response["job"]["id"]
        while True:
            job_response = get_request(get_url('jobs', job_id))
            if job_response and job_response["job"]["result"] and job_response["job"]["query_result_id"]:
                query_result_id = job_response["job"]["query_result_id"]
                update_response = get_request(get_url('query_results', query_result_id))
                if update_response:
                    logging.info(f"Query ID {query_id} updated.")
                break
            time.sleep(1)
    else:
        logging.error(f"Failed to refresh query ID {query_id}.")

def refresh_base_queries():
    """
    Refreshes the base queries defined in the configuration.

    Description:
        This function iterates over the list of base query IDs and refreshes each one using the refresh_widget function.
    """
    logging.info("Started refresh_base_queries()")
    for query_id in BASE_QUERY_IDS:
        refresh_widget(query_id)

def main_t():
    """
    Main function to coordinate the refresh process.

    Description:
        This function performs the initial refresh of base queries, then calls the scripts for owner query refresh and the scheduler.
    """
    current_time = datetime.datetime.now()
    logging.info(f"{current_time}\n")
    logging.info("Performing initial refresh...")
    refresh_base_queries()
    logging.info("Base queries refreshed. Now calling owner query refresh script...")
    subprocess.run(["python3", "owner_query_refresh.py"])
    logging.info("Owner queries refreshed. Now calling the scheduler...")
    subprocess.run(["python3", "scheduler.py"])

if __name__ == "__main__":
    main_t()
