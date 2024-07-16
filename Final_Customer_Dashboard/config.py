# config.py


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Base API URL
BASE_URL = "https://trustonic.thirdray.app/api"

# Headers for requests
HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en;q=0.5",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "remember_token=20-b79689cf11b1f162697d5d580c8b59ed|6a52e7a44ff4faef8ab669f17f12f32db5ea3abc9e3e05af1f188f3674e40b4160762da97af3eb5535ae54343b12574e497ba862103defe80fcc6b242ee3c7f8; session=.eJwlj0tqAzEQRO-itQMttVpS-zJDf4kxJDBjr0LuHkHWRb1X9VOOPOP6LPfX-Y5bOR5e7sWgE9Ka0nq0hkC62hTXvlSwOVYIJzQCRkbpDfvwEEdDrxYZFdpI6MNSU8CkUSzaLJ_OWJU3B2OlwU62yVhIApLCVHj6LLdi15nH6_sZX3uPcLbZZ1UjGbyEh8ukahXV59JkEUhU3r33Fef_iQYfOnkstqxVa9bRxoaT0wJbShxefv8A7iFJKQ.ZnAPgw.P-jWWVlQVqpwH2hk-y4MyJ7mfes; csrf_token=ImE5ZjI3NDcxYmM1YTY5OGE5NmRhNzUxYzEzYmQ3OGJmOWFhMGYzYjki.ZnJksQ.hLvAqXbNOLJdTYB3tADUBRONVQU",
    "Host": "trustonic.thirdray.app",
    "Referer": "https://trustonic.thirdray.app/login",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Brave\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}

# Query IDs
BASE_QUERY_IDS = [307, 305, 303, 292, 259]

# Owner Queries URL
OWNERS_URL = f"{BASE_URL}/queries/283/dropdowns/307"

# Owner Queries IDs
QUERY_IDS = [283, 284, 286, 287, 285, 304, 306, 295]
MAX_WORKERS = 8

# Dashboard Refresh URLs
QUERY_URL = f"{BASE_URL}/queries/{{}}/results"
JOB_URL = f"{BASE_URL}/jobs/{{}}"
UPDATE_DASHBOARD_URL = f"{BASE_URL}/query_results/{{}}"

# Refresh time
REFRESH_TIME = "12:19"  # Time in HH:MM format