from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Open the URL
driver.get('http://localhost:8080')

# Keep the browser open for a few seconds
driver.implicitly_wait(10)

# Close the browser
driver.quit()
