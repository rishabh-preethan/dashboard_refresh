FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements.txt (if you have dependencies)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the scheduler script
COPY scheduler.py .
COPY constants.properties .
COPY main.py .
COPY refresh_logic.py .
COPY utils.py .

EXPOSE 8080:8080

# Set the command to run the script
CMD ["python", "scheduler.py"]