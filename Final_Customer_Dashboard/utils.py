# utils.py


import requests
import time
import logging
from config import HEADERS

# HEADERS = {
#     "Accept": "application/json",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-GB,en;q=0.5",
#     "Cache-Control": "max-age=0",
#     "Connection": "keep-alive",
#     "Cookie": os.getenv("COOKIE"),
#     "Host": "trustonic.thirdray.app",
#     "Referer": "https://trustonic.thirdray.app/login",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-Fetch-User": "?1",
#     "Sec-GPC": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": os.getenv("USER_AGENT"),
#     "sec-ch-ua": os.getenv("SEC_CH_UA"),
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"macOS\""
# }

def get_url(endpoint, identifier):
    """
    Constructs the URL for the given API endpoint and identifier.

    Args:
        endpoint (str): The API endpoint.
        identifier (str or int): The identifier for the specific resource.

    Returns:
        str: The constructed URL.

    Description:
        This function constructs a URL for a given API endpoint and identifier,
        based on the base URL of the API.
    """
    return f"https://trustonic.thirdray.app/api/{endpoint}/{identifier}"

def post_request(url, payload, retry_count=3, delay=2):
    """
    Sends a POST request to the specified URL with the given payload.

    Args:
        url (str): The URL to which the POST request is sent.
        payload (dict): The payload to be sent in the POST request.
        retry_count (int): The number of retry attempts in case of failure (default is 3).
        delay (int): The delay in seconds between retry attempts (default is 2).

    Returns:
        dict or None: The JSON response from the server if the request is successful, None otherwise.

    Description:
        This function sends a POST request to the specified URL with the given payload.
        It retries the request in case of failure, logging errors and retry attempts.
    """
    while retry_count > 0:
        try:
            # Send the POST request with the payload and headers
            response = requests.post(url, json=payload, headers=HEADERS)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # Log the error and retry if retries are left
            logging.error(f"POST request failed: {e} - Retrying {retry_count - 1} more times")
            retry_count -= 1
            time.sleep(delay)
    # Log a critical error if the request ultimately fails
    logging.critical(f"POST request to {url} finally failed")
    return None

def get_request(url, retry_count=3, delay=2):
    """
    Sends a GET request to the specified URL.

    Args:
        url (str): The URL to which the GET request is sent.
        retry_count (int): The number of retry attempts in case of failure (default is 3).
        delay (int): The delay in seconds between retry attempts (default is 2).

    Returns:
        dict or None: The JSON response from the server if the request is successful, None otherwise.

    Description:
        This function sends a GET request to the specified URL.
        It retries the request in case of failure, logging errors and retry attempts.
    """
    while retry_count > 0:
        try:
            # Send the GET request with the headers
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # Log the error and retry if retries are left
            logging.error(f"GET request failed: {e} - Retrying {retry_count - 1} more times")
            retry_count -= 1
            time.sleep(delay)
    # Log a critical error if the request ultimately fails
    logging.critical(f"GET request to {url} finally failed")
    return None
