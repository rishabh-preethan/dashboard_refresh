FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements.txt (if you have dependencies)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the scheduler script
COPY scheduler.py .
COPY base_query_refresh.py .
COPY config.py .
COPY fetch_owners.py .
COPY utils.py .
COPY owner_query_refresh.py .

EXPOSE 8080:8080

# Set the command to run the script
CMD ["python", "scheduler.py"]