# Car Listings Scraper Web App

This web app allows users to scrape car listings from Kijiji based on specific criteria such as make, model, and price range, and receive email updates for new listings every 24 hours.

## Getting Started

Follow these steps to get the web app up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the web app, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://davidd3web/car-listings-scraper.git
cd car-listings-scraper
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Set up your .env file in the root directory with the following environment variables:
   SMTP_USER=your_email@gmail.com
   SMTP_PASS=your_app_password

## Using Gmail for SMTP

If you are using Gmail's SMTP server and have two-factor authentication enabled on your account, you need to create an App Password to use in place of your regular password. Follow these steps to create an App Password:

1. Go to your Google Account settings.
2. Under the "Security" tab, look for "Signing in to Google."
3. Select "App Passwords" (you may need to sign in again).
4. At the bottom, choose "Select app" and "Other (Custom name)."
5. Enter the name of your app (e.g., "Car Listings Scraper") and then select "Generate."
6. Use the generated 16-character password in your .env file as the SMTP_PASS.

### Running the APP

To run the web app, execute the following command in the frontend directory:

```bash
cd frontend
npm start
```

To run the web app, execute the following command in the backend directory:

```bash
cd backend
python create_db.py
flask run
```
