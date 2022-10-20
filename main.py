import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path='drivers/geckodriver')

# Opens the login website
driver.get('https://gne2.gndec.ac.in/login#login')

time.sleep(2)

# Enters the Username
username = driver.find_element(By.XPATH, '//*[@id="login_email"]')
username.send_keys('USERNAME')

time.sleep(1)

# Enters the Password
password = driver.find_element(By.XPATH, '//*[@id="login_password"]')
password.send_keys('PASSWORD')

time.sleep(1)

# Clicks the login button
login = driver.find_element(By.XPATH, '//*[@id="page-login"]/div/main/div[2]/div/section[1]/div[1]/form/div[2]/button')
login.click()

time.sleep(2)

# Read CSV file
with open('data/data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for line in csv_reader:

        # Redirects to new form website
        driver.get('https://gne2.gndec.ac.in/auto-fill-test?new=1')

        time.sleep(1)

        # Enters the name field of form
        name = driver.find_element(By.XPATH, '//*[@id="page-auto-fill-test"]/div/main/div[2]/div/div/div[2]/div/div[2]/div/div/div/form/div[1]/div/div[2]/div[1]/input')
        name.send_keys(line[0])

        time.sleep(1)

        # Enters the age field of form
        age = driver.find_element(By.XPATH, '//*[@id="page-auto-fill-test"]/div/main/div[2]/div/div/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[2]/div[1]/input')
        age.send_keys(line[1])

        time.sleep(1)

        # Enters the score field of form
        score = driver.find_element(By.XPATH, '//*[@id="page-auto-fill-test"]/div/main/div[2]/div/div/div[2]/div/div[2]/div/div/div/form/div[3]/div/div[2]/div[1]/input')
        score.send_keys(line[2])

        time.sleep(1)

        # Submits the form by clicking on submit button
        submit = driver.find_element(By.XPATH, '//*[@id="page-auto-fill-test"]/div/main/div[2]/div/div/div[3]/button')
        submit.click()

        time.sleep(2)

driver.close()
