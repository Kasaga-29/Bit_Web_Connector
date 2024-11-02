import os
import time
import subprocess
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import logging

login_url = 'http://10.0.0.55/srun_portal_pc?ac_id=8&theme=bit'

def create_log_file(log_file_path):
    logger = logging.getLogger('BitWebConnector')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def trim_log_file(log_file_path, log_max_line):
    with open(log_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if len(lines) > log_max_line:
        num_lines_to_delete = max(1, len(lines) // 5)
        lines = lines[num_lines_to_delete:]

    with open(log_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def check_internet_connection(test_url):
    process = subprocess.Popen(['ping', test_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode == 0

def bit_web_connector(username, password, sleep_time, edge_driver_path, test_url='www.baidu.com', offline_cnt_max=12, log_max_line=1000, log_file_path=None):
    offline_cnt = 0
    service = Service(executable_path=edge_driver_path)
    options = Options()
    options.add_argument('--headless')

    if log_file_path != None:
        logger =create_log_file(log_file_path)

    while True:
        if log_file_path != None:
            trim_log_file(log_file_path, log_max_line)
            
        is_connected = check_internet_connection(test_url)
        if is_connected:
            offline_cnt = 0
        else:
            offline_cnt += 1
            if offline_cnt > offline_cnt_max:
                if log_file_path != None:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logger.info(f"[Error]   | {current_time} | Please check your configuration and network connection. Offline for {offline_cnt_max * sleep_time / 60} minutes.")
                break
            
            if log_file_path != None:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logger.info(f"[Warning] | {current_time} | No internet connection. Attempting to log in...")

            driver = webdriver.Edge(service=service, options=options)
            wait = WebDriverWait(driver, 2)
            driver.get(login_url)

            try:
                username_box = wait.until(EC.presence_of_element_located((By.ID, 'username')))
            except TimeoutException:
                if log_file_path != None:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logger.info(f"[Error]   | {current_time} | Can not open Bit Web Page. Please check your network connection.")
                driver.quit()
                continue

            username_box.send_keys(username)
            password_box = driver.find_element(By.ID, 'password')
            password_box.send_keys(password)
            password_box.send_keys(Keys.RETURN)

            try:
                error_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'layui-layer-content')))
                error_message = error_element.text
                if log_file_path != None:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logger.info(f"[Error]   | {current_time} | {error_message}")
                driver.quit()
                break

            except TimeoutException:
                pass

            try:
                sign_out_element = wait.until(EC.presence_of_element_located((By.ID, 'logout')))
                if log_file_path != None:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logger.info(f"[Info]    | {current_time} | Successfully login in.")

            except TimeoutException:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if log_file_path != None:
                    logger.info(f"[Error]   | {current_time} | Unsuccessfully login in.")
                    driver.quit()
                break
            
            driver.quit()

        time.sleep(sleep_time)
            

if __name__ == '__main__':
    username = '1120250001'
    password = '12345678'
    sleep_time = 300
    bit_web_connector(username, password, sleep_time)