# owner_query_refresh.py


import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor, as_completed
from fetch_owners import fetch_owners
from utils import get_url, post_request, get_request
from config import QUERY_IDS, MAX_WORKERS

# logging.basicConfig(
#     filename='//home//rishabhp//sandbox//Final_Customer_Dashboard//app.log',  # Path to the log file
#     filemode='a',  # Append mode
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
#     level=logging.INFO  # Log level
# )

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_email(total_time):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'rishabhp5902@gmail.com'  # Your Gmail address
    smtp_password = 'nxylukdppgtfrjwr'     # App-specific password

    # List of recipient email addresses
    to_addresses = ['rishabh.preethan@gmail.com', 'raycario5500@gmail.com', 'rishabh_preethan@thirdray.ai']

    # Create SMTP server object
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:
        # Login to the SMTP server with app-specific password
        server.login(smtp_username, smtp_password)

        # Compose and send the email
        from_address = 'rishabhp5902@gmail.com'
        subject = 'Refresh Completed for Final Dashboard'
        body = 'Refresh for Final Dashboard V2 has been completed'

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

def refresh_widget(p_owner, query_id, retry_count=3):
    """
    Refreshes the widget for the given owner and query ID.

    Args:
        p_owner (str): The owner for whom the query is being refreshed.
        query_id (int): The ID of the query to be refreshed.
        retry_count (int): The number of times to retry the request in case of failure (default is 3).

    Description:
        This function sends a POST request to refresh the widget associated with the given owner and query ID.
        It then polls the job status until the query result is updated.
    """
    logging.info(f"Starting refresh for owner: {p_owner}, query ID: {query_id}")
    payload = {
        "id": query_id,
        "parameters": {"owner": p_owner},
        "apply_auto_limit": True,
        "max_age": 0
    }
    # Add specific parameters for query ID 295
    if query_id == 295:
        payload["parameters"]["last12months"] = {"start": "2023-06-27", "end": "2024-06-27"}
        payload["parameters"]["brand"] = ["SAMSUNG"]

    results_url = get_url('queries', query_id) + '/results'
    response = post_request(results_url, payload, retry_count)

    if response and "job" in response:
        job_id = response["job"]["id"]
        while True:
            job_response = get_request(get_url('jobs', job_id))
            if job_response and job_response["job"]["result"] and job_response["job"]["query_result_id"]:
                query_result_id = job_response["job"]["query_result_id"]
                update_response = get_request(get_url('query_results', query_result_id))
                if update_response:
                    logging.info(f"Query ID {query_id} updated for owner {p_owner}.")
                break
            time.sleep(0.5)
    else:
        logging.error(f"Failed to refresh query ID {query_id} for owner {p_owner}")

def refresh_dashboard_for_owner(p_owner):
    """
    Refreshes the dashboard for the given owner by refreshing all associated queries.

    Args:
        p_owner (str): The owner for whom the dashboard is being refreshed.

    Description:
        This function uses a thread pool to refresh all queries associated with the given owner concurrently.
    """
    logging.info(f"Starting dashboard refresh for owner: {p_owner}")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit refresh tasks for all queries of the owner
        futures = {executor.submit(refresh_widget, p_owner, query_id): query_id for query_id in QUERY_IDS}
        for future in as_completed(futures):
            query_id = futures[future]
            try:
                future.result()
            except Exception as e:
                logging.error(f"Exception occurred for query ID {query_id}: {e}")

def refresh_all_dashboards():
    """
    Refreshes dashboards for all owners.

    Description:
        This function fetches all owners and then uses a thread pool to refresh the dashboard for each owner concurrently.
        It logs the total time taken to complete the refresh for all owners.
    """
    logging.info("Starting dashboard refresh for all owners")
    owners = fetch_owners()
    if owners:
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # Submit refresh tasks for all owners
            futures = [executor.submit(refresh_dashboard_for_owner, owner["value"]) for owner in owners]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Exception occurred: {e}")
        end_time = time.time()
        total_time = end_time - start_time
        logging.info(f"Total time taken to refresh all owners: {end_time - start_time:.2f} seconds")
        
        # Send an email notification
        subject = "Dashboard Refresh Completed"
        body = f"The dashboard refresh process has completed successfully. Total time taken: {total_time:.2f} seconds."
        send_email(total_time)

if __name__ == "__main__":
    # Start the refresh process for all dashboards
    refresh_all_dashboards()
