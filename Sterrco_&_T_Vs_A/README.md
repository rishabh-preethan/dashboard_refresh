
# Widget Refresh Application

## Overview

This application performs an initial refresh of all widgets and schedules daily refreshes. It is designed to fetch updated data for specified widgets by making API calls, processing the data, and handling retries in case of failures.

## Components

1. **constants.properties**: Configuration file storing constants like query IDs, headers, and the refresh schedule.
2. **main.py**: Entry point for the application. It performs an initial refresh and schedules daily refreshes.
3. **refresh_logic.py**: Contains logic for refreshing widgets by making API calls.
4. **scheduler.py**: Manages the scheduling of the daily refresh tasks.
5. **utils.py**: Utility functions used across the application.

## Configuration

The `constants.properties` file contains the following sections:

### [DEFAULT]

- `BASE_QUERY_IDS`: Comma-separated list of base query IDs to refresh.
- `TIME_REFRESH_SCHEDULE`: Time in IST (HH:MM) to schedule the daily refresh.

### [HEADERS]

Contains headers for the API requests.

## How It Works

### Initial Refresh

1. **main.py**:
   - Loads configuration.
   - Performs an initial refresh by calling `refresh_all_widgets`.

### Refresh Logic

2. **refresh_logic.py**:
   - `refresh_widget`: Makes a POST request to refresh a specific widget. Retries in case of failure.
   - `refresh_base_queries`: Refreshes base queries in a specified sequence.
   - `refresh_all_widgets`: Wrapper to call `refresh_base_queries`.

### Scheduling

3. **scheduler.py**:
   - `schedule_refresh`: Schedules daily refresh using the `schedule` module. Converts IST time to server's local time.
   - Starts a loop to run pending scheduled tasks.

### Utilities

4. **utils.py**:
   - `get_url`: Constructs API URLs for different endpoints.

## Flowchart
https://www.mermaidchart.com/raw/89700cbc-f658-48f3-83f9-17910c11504d?theme=dark&version=v0.1&format=svg

## Running the Application

1. Ensure `constants.properties` is correctly configured.
2. Run the application:
   ```bash
   python main.py
   ```

## Analytical Table
|No.of Exp   | Date         | Start Time(IST)| Time Taken          | Refreshed all or not  | Dashboard                 |
|------------|--------------|----------------|---------------------|-----------------------|---------------------------|
|1           |28-June-2024  | 21:30          |184 seconds = 3 mins |   All Refreshed       | STERRCO & Target vs Actual|
|2           |28-June-2024  | 21:35          |182 seconds = 3 mins |   All Refreshed       | STERRCO & Target vs Actual|
|3           |28-June-2024  | 21:39          |180 seconds = 3 mins |   All Refreshed       | STERRCO & Target vs Actual|
|4           |29-June-2024  | 9:30           |181 seconds = 3 mins |   All Refreshed       | STERRCO & Target vs Actual|
|5           |29-June-2024  | 9:37           |182 seconds = 3 mins |   All Refreshed       | STERRCO & Target vs Actual|
|6           |30-June-2024  | 21:30          |193 seconds = 3 mins |   All Refreshed       | STERRCO & Target vs Actual|

This will perform an initial refresh and start the scheduler for daily refreshes.