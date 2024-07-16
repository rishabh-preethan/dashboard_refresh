import requests
import time
from utils import get_url
import configparser
import logging
import smtplib

# Load constants from the properties file
config = configparser.ConfigParser()
config.read('constants.properties')

BASE_QUERY_IDS = [int(x) for x in config.get('DEFAULT', 'BASE_QUERY_IDS').split(',')]
HEADERS = {k: v for k, v in config.items('HEADERS')}

logging.basicConfig(
    filename='app.log',  # Path to the log file
    filemode='a',  # Append mode
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO  # Log level
)

def send_email(subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'rishabhp5902@gmail.com'  # Your Gmail address
    smtp_password = 'nxylukdppgtfrjwr'     # App-specific password

    # List of recipient email addresses
    to_addresses = ['aditi_l@thirdray.ai', 'rishabh_preethan@thirdray.ai', 'akhile@thirdray.ai', 'meera@thirdray.ai']

    # Create SMTP server object
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:
        # Login to the SMTP server with app-specific password
        server.login(smtp_username, smtp_password)

        # Compose and send the email
        from_address = smtp_username
        for to_address in to_addresses:
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(from_address, to_address, message)
            print(f"Email sent successfully to {to_address}!")
            logging.info(f"Email sent successfully to {to_address}!")

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
        logging.info(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        logging.info(f"Failed to send email. Error: {e}")

    finally:
        server.quit()

def refresh_widget(query_id, parameters=None, retry_count=3):
    """
    Refresh a specific widget by its query ID.

    Parameters:
    - query_id (int): The ID of the query to refresh.
    - parameters (dict, optional): Additional parameters for the query. Defaults to None.
    - retry_count (int, optional): Number of retry attempts in case of failure. Defaults to 3.

    This function makes a POST request to initiate the refresh and checks the job status until it completes.
    """
    print(f"Starting refresh for query ID: {query_id}")  # Print statement when refresh starts
    logging.info(f"Starting refresh for query ID: {query_id}")

    payload = {
        "id": query_id,
        "parameters": parameters or {},
        "apply_auto_limit": True,
        "max_age": 0
    }

    try:
        response = requests.post(get_url('queries', query_id) + '/results', json=payload, headers=HEADERS)
        response.raise_for_status()
        job_id = response.json().get("job", {}).get("id")

        if not job_id:
            error_message = f"No job found in the response for query ID {query_id}."
            print(error_message)
            logging.info(error_message)
            return False, error_message

        while True:
            job_response = requests.get(get_url('jobs', job_id), headers=HEADERS).json()
            if job_response["job"]["result"] and job_response["job"]["query_result_id"]:
                query_result_id = job_response["job"]["query_result_id"]
                update_response = requests.get(get_url('query_results', query_result_id), headers=HEADERS)
                update_response.raise_for_status()
                success_message = f"Query ID {query_id} updated."
                print(success_message)
                logging.info(success_message)
                return True, None
            time.sleep(2)
    except requests.RequestException as e:
        error_message = f"Failed to refresh query ID {query_id}: {e}"
        print(error_message)
        logging.info(error_message)
        if retry_count > 0:
            retry_message = f"Retrying... ({retry_count} attempts left)"
            print(retry_message)
            logging.info(retry_message)
            time.sleep(2)
            return refresh_widget(query_id, parameters, retry_count - 1)
    except Exception as e:
        error_message = f"Exception occurred while refreshing query ID {query_id}: {e}"
        print(error_message)
        logging.info(error_message)
        return False, error_message

    return False, error_message

def refresh_base_queries():
    """
    Refresh base queries in a specific sequence:
    Refresh queries with IDs 722 and 651 first, then proceed to 635.

    This function calls `refresh_widget` for each base query ID.
    """
    for query_id in BASE_QUERY_IDS[:2]:  # Refresh first two queries (722 and 651)
        success, error_message = refresh_widget(query_id)
        if not success:
            send_email(
                subject='Refresh Failed for Steerco Dashboard',
                body=f'Refresh for Steerco Dashboard failed for query ID {query_id}\nError: {error_message}'
            )
            return False
    success, error_message = refresh_widget(BASE_QUERY_IDS[2])  # Refresh the third query (635) after the first two
    if not success:
        send_email(
            subject='Refresh Failed for Steerco Dashboard',
            body=f'Refresh for Steerco Dashboard failed for query ID {BASE_QUERY_IDS[2]}\nError: {error_message}'
        )
        return False
    return True

def refresh_all_widgets():
    """
    Refresh all widgets by calling the function to refresh base queries.

    This function serves as a wrapper to refresh base queries.
    """
    # Calculating total time taken for refresh then logging it
    start_time = time.time()
    if refresh_base_queries():
        end_time = time.time()
        total_time = end_time - start_time
        logging.info(f"Total time taken is {total_time}")
        send_email(
            subject='Refresh Completed for Steerco Dashboard',
            body=f'Refresh for Steerco Dashboard has been completed. Total time taken is {total_time} seconds.'
        )
    else:
        logging.info("Refresh failed for one or more queries.")
