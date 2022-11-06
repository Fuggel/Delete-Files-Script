"""System module."""
import time
import os

DOWNLOAD_PATH = "C:/Users/Furkan Ceylan/Downloads"
GIGABYTE = 1073741824
ALLOWED_TIME_SEC = 60 * 60  # 1 hour

while True:
    # Iterate directory
    for path in os.listdir(DOWNLOAD_PATH):
        full_path = DOWNLOAD_PATH + "/" + path

        if os.path.isfile(os.path.join(DOWNLOAD_PATH, path)):
            modified_date = os.path.getctime(full_path)

            check_time = ((int(time.time()) - modified_date) > ALLOWED_TIME_SEC)
            check_size = (os.path.getsize(full_path) < GIGABYTE)

            if check_time and check_size:
                os.remove(full_path)

    time.sleep(60)
