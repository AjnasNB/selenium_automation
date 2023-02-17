from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# List of recipients' phone numbers
recipients = ['1234567890', '0987654321']

# Message to send to each recipient
message = 'Hello from Python!'

# Initialize Chrome driver
driver = webdriver.Chrome('./chromedriver')

# Load WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for user to log in and scan QR code
input('Press Enter once you have logged in and scanned the QR code.')

# Send a message to each recipient
for recipient in recipients:
    # Find the search box and enter the recipient's name
    search_box = driver.find_element_by_xpath("//div[contains(@class, 'copyable-text selectable-text')][@data-tab='3']")
    search_box.send_keys(recipient)
    time.sleep(2)

    # Press Enter to open the chat with the recipient
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Find the message box and enter the message
    message_box = driver.find_element_by_xpath("//div[contains(@class, 'copyable-text selectable-text')][@data-tab='1']")
    message_box.send_keys(message)
    time.sleep(2)

    # Find the send button and click it
    send_button = driver.find_element_by_xpath("//span[@data-icon='send']")
    send_button.click()
    time.sleep(2)

    print(f'Message sent to {recipient}')

# Close the browser
driver.quit()
