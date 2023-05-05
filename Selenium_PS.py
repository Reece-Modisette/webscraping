from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to Career Shift's login page
driver.get("https://www.careershift.com/default.cfm")

# Find the username and password input fields and enter your credentials
username_field = driver.find_element_by_name("UserEmail")
username_field.send_keys("reece_modisette1@baylor.edu")
password_field = driver.find_element_by_name("Password")
password_field.send_keys("MarineCorp2024!")

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for the login to complete and the dashboard page to load
dashboard_title = "CareerShift - Dashboard"
assert driver.title == dashboard_title

# Close the browser
driver.quit()


