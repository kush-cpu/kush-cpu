import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Function to send messages
def send_whatsapp_message(contact, message):
    driver = webdriver.Chrome("path_to_chromedriver")  # Update with the path to your Chrome WebDriver
    driver.get("https://web.whatsapp.com/")
    input("Please scan QR code and press Enter once logged in")
    time.sleep(5)  # Let WhatsApp web load completely

    # Locate the search box
    search_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text")]')
    search_box.click()
    search_box.send_keys(contact)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Locate the message input box
    message_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text")]')
    message_box.click()
    message_box.send_keys(message)
    time.sleep(1)
    message_box.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.quit()

# Read contacts from CSV and send messages
def send_bulk_messages(csv_file, message):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contact = row['phone_number']  # Assuming 'phone_number' is the header for phone numbers
            custom_message = f"Hello {row['name']}, {message}"  # Assuming 'name' is the header for contact names
            send_whatsapp_message(contact, custom_message)
            print(f"Message sent to {row['name']}")

# Example usage
if __name__ == "__main__":
    csv_file = "contacts.csv"  # Update with the path to your CSV file
    message = "This is a custom message."  # Your custom message here
    send_bulk_messages(csv_file, message)
