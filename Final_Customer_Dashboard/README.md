# Query Refresh Automation

This repository contains scripts to automate the refresh of query widgets and dashboards. The scripts are designed to fetch data from an API, refresh widgets for various queries, and schedule these refresh tasks to run periodically.

## Table of Contents

- [Overview](#overview)
- [Configuration](#configuration)
- [Scripts](#scripts)
- [Flowchart](#flowchart)
- [How to Use](#how-to-use)

## Overview

The automation consists of several components:
1. **Base Query Refresh**: Refreshes a set of predefined base queries.
2. **Owner Query Refresh**: Refreshes queries for different owners.
3. **Scheduler**: Schedules the refresh tasks to run at a specified time daily.

## Configuration

Configuration settings and environment variables are stored in `config.py` file. Key configuration items include:
- `BASE_URL`: The base URL for the API.
- `HEADERS`: Headers for API requests.
- `BASE_QUERY_IDS`: IDs of the base queries to refresh.
- `QUERY_IDS`: IDs of the queries for owner-specific refresh.
- `OWNERS_URL`: URL to fetch the list of owners.
- `REFRESH_TIME`: The time to run the scheduled refresh tasks (in HH:MM format).

## Scripts

- `base_query_refresh.py`: Refreshes the base queries.
- `owner_query_refresh.py`: Refreshes queries for different owners.
- `scheduler.py`: Schedules the refresh tasks to run at a specified time.
- `fetch_owners.py`: Fetches the list of owners from the API.
- `utils.py`: Utility functions for making API requests.

## Flowchart

https://www.mermaidchart.com/raw/89700cbc-f658-48f3-83f9-17910c11504d?theme=dark&version=v0.1&format=svg


## Analytical Table
| No.of Exp | Date      | Start Time(IST) | Time Taken               | Max - Workers| Batch - size | Refreshed all or not  | Dashboard      |
|-----------|-----------|-----------------|--------------------------|--------------|--------------|-----------------------|----------------|
|1          |27-Jun-2024| 15:28           |5054.60 seconds=1hr40min  |       3      |      -       | All Refreshed         | Final Customer |
|2          |27-Jun-2024| 17:00           |5119.72 seconds=1hr42min  |       5      |      -       | All Refreshed         | Final Customer |
|3          |27-Jun-2024| 19:20           |3145.29 seconds = 52 min  |       8      |      -       | All Refreshed         | Final Customer |
|4          |27-Jun-2024| 21:00           |3160.22 seconds = 52 min  |       9      |      -       | All Refreshed         | Final Customer |
|5          |28-Jun-2024| 08:50           |3155 seconds = 52 min     |      10      |      -       | All Refreshed         | Final Customer |
|6          |28-Jun-2024| 10:20           |3684 seconds = 61 mins    |      10      |      -       | All Refreshed         | Final Customer |
|7          |28-Jun-2024| 17:38           |3131.93 seconds = 52 mins |       8      |     10       | Not All refreshed(23!)| Final Customer |
|8          |29-Jun-2024| 21:30           |3156.29 seconds = 52 mins |       8      |      -       | All Refreshed         | Final Customer |
|9          |29-Jun-2024| 22:50           |3146.29 seconds = 52 mins |       8      |      -       | All Refreshed         | Final Customer |
|10         |30-Jun-2024| 09:30           |3046.45 seconds = 50 mins |       9      |      -       | All Refreshed         | Final Customer |

The First 2 experiments is with query_id 365, other 8 are without query_id 365# dashboard_refresh
