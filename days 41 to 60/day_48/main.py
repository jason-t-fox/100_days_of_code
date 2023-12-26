# challenge to pull PyCon events

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# event_days = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time") # replaced below
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_years_selector = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

event_days = []

for element in event_years_selector:
    event_timestamp = element.get_attribute('datetime')
    event_dates = datetime.strptime(event_timestamp, "%Y-%m-%dT%H:%M:%S%z").date()
    event_days.append(event_dates.strftime("%Y-%m-%d"))


events = {}

for n in range(len(event_names)):
    events[n] = {
        "date": event_days[n],
        "name": event_names[n].text
    }

print(events)

driver.quit()
