# utils.py

"""
Utility functions for the application.
"""

def get_url(endpoint, identifier):
    """
    Construct the API URL for a given endpoint and identifier.

    Parameters:
    - endpoint (str): The API endpoint (e.g., 'queries', 'jobs', 'query_results').
    - identifier (int): The specific ID for the endpoint.

    Returns:
    - str: The full URL for the API request.
    """
    return f"https://trustonic.thirdray.app/api/{endpoint}/{identifier}"
