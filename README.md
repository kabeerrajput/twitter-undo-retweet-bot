**Twitter Undo Retweet Bot**

A Python automation bot that automatically logs into Twitter (X) and undoes your retweets using Selenium.
This bot is helpful if you want to bulk-remove retweets from your timeline without doing it manually.

⚡ **Features**

Automates Twitter login via Selenium
Navigates to your profile
Detects all retweets in your timeline
Clicks Undo Retweet one by one until none remain
Scrolls automatically to load more retweets
Handles loading spinners and delays gracefully

🛠️ **Requirements**

Python 3.8+
Google Chrome (latest version recommended)
ChromeDriver (must match your Chrome version)

⚙️ **Setup**

1: Clone the repository:
git clone https://github.com/kabeerrajput/Twitter_Undo_Retweet_Bot.git
cd Twitter_Undo_Retweet_Bot

2: Make sure ChromeDriver is installed and in your PATH.
Download ChromeDriver
Run the bot with
python main.py


**The bot will**:

Open Chrome
Go to Twitter login page
Enter your username and password
Navigate to your profile
Start undoing retweets automatically

Note: Update the username and password arguments in
login_and_navigate(username="", password="") inside TC_Twitter_Bot.py before running.

⚠️ **Important Notes**

Logging in with automation may trigger Twitter/X security checks.
Using this bot on a large scale may violate Twitter’s terms of service. Use at your own risk.
