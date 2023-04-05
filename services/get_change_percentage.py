import os
import time
from dotenv import load_dotenv
from selenium import webdriver
# smtplib module defines an SMTP client session object
# that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
import smtplib
# MIME (Multipurpose Internet Mail Extensions) is an extension of the original Simple Mail Transport Protocol (SMTP)
# email protocol. It lets users exchange different kinds of data files,
# including audio, video, images and application programs, over email.
from email.mime.text import MIMEText

# Selenium Webdriver is an open-source collection of APIs which is used for testing web applications.
# The Selenium Webdriver tool is used for automating web application testing to verify that it works as expected or not.

# Load env
load_dotenv()


def get_driver():
    options = webdriver.ChromeOptions()
    # Add a command-line argument to use when starting Chrome with instance method: add_argument(arg) ⇒ Object
    options.add_argument("disable-infobars")
    options.add_argument("start-maximize")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    # Adds an experimental option which is passed to chromium.
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver


def get_change_percentage(driver):
    from selenium.webdriver.common.by import By
    # elements = driver.find_element(By.ID, "app_indeks")
    element = driver.find_element(By.CLASS_NAME, "stock-trend")
    # OR find by xpath
    # element = driver.find_element(by="xpath", value="//*[@id='app_indeks']/section[1]/div/div/div[2]/span[2]")
    value = element.text.replace(" %", "")

    return float(value)


def send_email(receiver, value):
    sender = os.getenv('MY_EMAIL')
    pwd = os.getenv('MY_APP_PWD')
    mess = f"This is to inform you that the percentage change of the stock is {value}%"

    mess = MIMEText(mess)
    mess['From'] = sender
    mess['To'] = receiver
    mess['Subject'] = "Rate change notification"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, pwd)
    print("------Logging in------")
    time.sleep(2)
    server.sendmail(sender, receiver, mess.as_string())
    print("------Email sent------")
    server.quit()