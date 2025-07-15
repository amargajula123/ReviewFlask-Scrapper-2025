import os
from datetime import datetime


# ROOT_DIR = os.getcwd() # D:\ML_Projects\MLOps_California_House_Price_Prediction\housing\constant #os.getcwd() # to get current/root working directrory
# print(ROOT_DIR)
def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR = os.getcwd()  # to get current working directory
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

# print(CONFIG_FILE_PATH)

CURRENT_TIME_STAMP = get_current_time_stamp()