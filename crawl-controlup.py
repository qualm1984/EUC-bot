import selenium
selenium.__version__
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to the ControlUp Docs page
    driver.get('https://support.controlup.com/docs')

    # Ensure the navigation bar is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'categories')))

     # Find the navigation bar and extract href values of anchor tags inside it
    nav_bar = driver.find_element(By.ID, 'categories')
    links = nav_bar.find_elements(By.TAG_NAME, 'a')
    extracted_hrefs = [link.get_attribute('href') for link in links if link.get_attribute('href') is not None]

    # Write the extracted URLs into a text file
    with open("controlup-docs.txt", 'w', encoding='utf-8') as f:
        for href in extracted_hrefs:
            f.write(href + "\n")

    print(f"Wrote {len(extracted_hrefs)} URLs to controlup-docs.txt")

finally:
    driver.quit()
