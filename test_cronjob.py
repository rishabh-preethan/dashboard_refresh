import datetime

def log_time():
    with open("time_log.txt", "a") as file:
        current_time = datetime.datetime.now()
        file.write(f"{current_time}\n")

if __name__ == "__main__":
    log_time()
