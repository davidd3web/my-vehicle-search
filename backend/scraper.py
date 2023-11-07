import requests
import time
from app import app
from bs4 import BeautifulSoup
from models import db, UserInput

from dotenv import load_dotenv
import os

load_dotenv()  # This loads the .env file at the application start

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

base_url = "https://www.kijiji.ca"

def build_url(make, model, price, any_model):
    if any_model:
        return f"{base_url}/b-cars-trucks/calgary/c174l1700199?for-sale-by=ownr&price=__{price}"
    else:
        return f"{base_url}/b-cars-vehicles/calgary/{make}-{model}/c174l1700199?for-sale-by=ownr&price=__{price}"

def scrape_for_user(user):
    url = build_url(user.make, user.model, user.price, user.anyModel)
    response = requests.get(url)
    ads_list = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        ads = soup.find_all("section", attrs={"data-testid": ["listing-card"]})

        for ad in ads:
            title_element = ad.find(attrs={"data-testid": "listing-title"})
            price_element = ad.find(attrs={"data-testid": "listing-price"})
            link_element = ad.find(attrs={"data-testid": "listing-link"})
            link = link_element['href'] if link_element and 'href' in link_element.attrs else None
            full_link = f"{base_url}{link}" if link else None
            
            # If the elements are found, extract the text
            title = title_element.get_text(strip=True) if title_element else "No Title"
            price = price_element.get_text(strip=True) if price_element else "No Price"

            ads_list.append((title, price, full_link))

        if ads_list:
          send_email(user.email, ads_list)
        else:
          print(f"No listings found for {user.email}")


    else:
        print(f"Failed to retrieve data for {user.email}")

def send_email(user_email, ads_list):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'

    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASS')
    
    
    # Email content
    subject = "New car listing found!"
    body = "<h1>New Listing Found</h1>"
    for title, price, link in ads_list:
      body += f"<p><b>Title:</b> {title}<br><b>Price:</b> {price}<br><b>Link:</b> <a href='{link}'>View Listing</a></p><hr>"
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = smtp_user
    message['To'] = user_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))
    
    # Send the email
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(message)
    server.quit()

    print(f"Email sent to {user_email}")

def scrape_all_users():
    all_users = UserInput.query.all()
    for user in all_users:
        scrape_for_user(user)

# Assuming you would call this function to start scraping for all users
if __name__ == '__main__':
    try:
        with app.app_context():
          while(True):
            scrape_all_users()
            time.sleep(86400)
    except Exception as e:
        print(f"An error occurred: {e}")
