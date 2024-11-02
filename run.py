from login import bit_web_connector

username = '1120250001'
password = '12345678'
interval = 300
edge_driver_path = 'C:/Your/Path/to/Bit_Web_Connector/edge_driver/msedgedriver.exe'
log_file_path = 'C:/Your/Path/to/Bit_Web_Connector/logger.log'

bit_web_connector(username=username, password=password, sleep_time=interval, edge_driver_path=edge_driver_path, log_file_path=log_file_path)

