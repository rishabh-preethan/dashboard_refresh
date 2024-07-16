# fetch_owners.py


import logging
from config import OWNERS_URL, HEADERS
import requests

# logging.basicConfig(
#     filename='//home//rishabhp//sandbox//Final_Customer_Dashboard//app.log',  # Path to the log file
#     filemode='a',  # Append mode
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
#     level=logging.INFO  # Log level
# )

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_owners():
    """
    Fetches the list of owners from the API.

    Returns:
        list: A list of dictionaries containing the name and value of each owner.

    Description:
        This function sends a GET request to the OWNERS_URL endpoint using the provided headers.
        It processes the response to extract owner names and values, returning them in a list.
        If the request fails, it logs an error and returns an empty list.
    """
    try:
        # Send a GET request to the owners URL
        response = requests.get(OWNERS_URL, headers=HEADERS)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Parse the JSON response
        owners_data = response.json()
        # Extract and return the owner names and values
        return [{"name": owner["name"], "value": owner["value"]} for owner in owners_data if owner["value"]]
    except requests.RequestException as e:
        # Log an error if the request fails
        logging.error(f"Failed to fetch owners: {e}")
        return []

if __name__ == "__main__":
    # Fetch and log the owners
    owners = fetch_owners()
    logging.info(f"Fetched owners: {owners}")
