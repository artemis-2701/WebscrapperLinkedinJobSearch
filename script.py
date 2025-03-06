import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# LinkedIn credentials
EMAIL = "your-email@example.com"
PASSWORD = "your-password"

# Set up Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

# Log in
email_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for login

# Go to LinkedIn Jobs
driver.get("https://www.linkedin.com/jobs/search/")
time.sleep(3)

# Enter Job Title
search_box = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
search_box.send_keys("IoT Engineer" + Keys.RETURN)
time.sleep(5)

# Set location to United States
location_box = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
location_box.clear()
location_box.send_keys("United States" + Keys.RETURN)
time.sleep(5)

# Set experience level to Internship
experience_filter = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Experience Level filter')]")
experience_filter.click()
time.sleep(2)
internship_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Internship')]/ancestor::label")
internship_option.click()
time.sleep(2)

# Apply filter
apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show results')]")
apply_button.click()
time.sleep(5)

# Get Job Titles and Links
jobs_data = []
jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
for job in jobs[:5]:  # Get first 5 jobs
    title = job.find_element(By.TAG_NAME, "h3").text
    link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
    jobs_data.append([title, link])

# Save results to a CSV file
with open("linkedin_jobs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Job Link"])
    writer.writerows(jobs_data)

print("✅ Jobs saved to linkedin_jobs.csv")

driver.quit()
