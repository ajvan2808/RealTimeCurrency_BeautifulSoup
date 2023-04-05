import time
# from services.get_currency import get_currency
from services.get_change_percentage import get_driver, get_change_percentage, send_email


if __name__ == '__main__':
    driver = get_driver()
    time.sleep(5)
    value = get_change_percentage(driver)
    if value > 0.1:
        send_email("vhh2808@gmail.com", value)